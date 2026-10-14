-- Pandoc filter for CERTA documents exported to PDF.
-- Moves title, subtitle, author, date, doctype and reference into LaTeX macros,
-- adds the preamble of certa-header.tex, replaces the default title with the
-- CERTA title block and resolves image paths relative to the document.

if not FORMAT:match("latex") then
  return {}
end

local dir = pandoc.path.directory(PANDOC_SCRIPT_FILE)
local logo = pandoc.path.normalize(pandoc.path.join({dir, "..", "..", "assets", "logo", "certa-logo.png"}))
local mark = pandoc.path.normalize(pandoc.path.join({dir, "..", "..", "assets", "logo", "certa-mark.png"}))
local input = PANDOC_STATE.input_files[1]
local input_dir = input and pandoc.path.directory(input) or "."
local MONTHS = {"January", "February", "March", "April", "May", "June", "July",
                "August", "September", "October", "November", "December"}

local function to_latex(value)
  if value == nil then
    return ""
  end
  local inlines = pandoc.utils.type(value) == "Inlines" and value or pandoc.Inlines(pandoc.utils.stringify(value))
  return (pandoc.write(pandoc.Pandoc({pandoc.Plain(inlines)}), "latex"):gsub("%s+$", ""))
end

local function list(value)
  if value == nil then
    return {}
  end
  return pandoc.utils.type(value) == "List" and value or {value}
end

function Meta(meta)
  local authors, plain_authors = {}, {}
  for _, a in ipairs(list(meta.author)) do
    table.insert(authors, to_latex(a))
    table.insert(plain_authors, pandoc.utils.stringify(a))
  end

  local date = meta.date and pandoc.utils.stringify(meta.date) or ""
  if date == "today" then
    local t = os.date("*t")
    date = string.format("%d %s %d", t.day, MONTHS[t.month], t.year)
  end

  local doctype, reference = to_latex(meta.doctype), to_latex(meta.reference)
  local running = to_latex(meta["running-title"] or meta.title)
  if reference ~= "" then
    running = reference .. " · " .. running
  end

  local macros = {
    certaTitle = to_latex(meta.title), certaSubtitle = to_latex(meta.subtitle),
    certaAuthor = table.concat(authors, ", "), certaDate = to_latex(date),
    certaDoctype = doctype, certaReference = reference, certaRunning = running,
    certaLogoPath = logo, certaMarkPath = mark,
  }
  local defs = {}
  for name, value in pairs(macros) do
    table.insert(defs, string.format("\\def\\%s{%s}", name, value))
  end

  local includes = meta["header-includes"]
  if includes == nil then
    includes = pandoc.MetaList({})
  elseif pandoc.utils.type(includes) ~= "List" then
    includes = pandoc.MetaList({includes})
  end
  local preamble = io.open(pandoc.path.join({dir, "certa-header.tex"})):read("a")
  includes:insert(pandoc.MetaBlocks({pandoc.RawBlock("latex", table.concat(defs, "\n") .. "\n" .. preamble)}))
  meta["header-includes"] = includes

  meta["title-meta"] = pandoc.utils.stringify(meta.title or "")
  meta["author-meta"] = table.concat(plain_authors, ", ")
  meta.title, meta.subtitle, meta.author, meta.date = nil, nil, nil, nil
  return meta
end

function Pandoc(doc)
  doc.blocks:insert(1, pandoc.RawBlock("latex", "\\certamaketitle"))
  return doc
end

function Image(img)
  if not img.src:match("^%a[%w+.-]*:") and not pandoc.path.is_absolute(img.src) then
    img.src = pandoc.path.normalize(pandoc.path.join({input_dir, img.src}))
  end
  return img
end

return {{Meta = Meta, Image = Image}, {Pandoc = Pandoc}}
