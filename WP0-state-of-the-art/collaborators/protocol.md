---
title: "Review protocol"
subtitle: "Selection of test points, stimuli and measurements for the test of analog circuits: a systematic mapping review"
author: "Telmo Miguel-Medina"
---

# 1. Aim and type of review

To map how the literature decides what to measure and what to apply in order to detect and locate faults in analog circuits, and how those decisions account for measurement cost, fault risk, tolerances and statistical support.

Systematic mapping review, without meta-analysis, reported according to PRISMA 2020 and PRISMA-S.

# 2. Review questions

| Id | Question |
|:--|:-------------------------------------------------------------|
| RQ1 | What is decided when the test is designed (nodes, stimuli, measurements), and jointly or separately? |
| RQ2 | How are the cost and the limitations of the measuring hardware modelled? |
| RQ3 | What objective is optimised? Are faults weighted by probability or severity, and are false alarms controlled? |
| RQ4 | How are tolerances treated, and with what statistical support are the metrics reported? |
| RQ5 | What is each method compared against, on which circuits, and how reproducible is the comparison? |
| RQ6 | Does any work combine embedded hardware cost, risk and statistical certification at board level? |

# 3. Sources

Scopus, Web of Science Core Collection and IEEE Xplore (metadata only), with no date limit, using the search strings in Appendix A. They are complemented with author searches and with backward and forward citation tracking of the control set (Appendix B) and of the included studies that score on three or more of the cross-cutting criteria of the classification scheme. No grey literature.

The control set is a list of 24 works that the search must retrieve; it is used to check the recall of the search strings.

# 4. Eligibility

A study is included if it meets I1 to I4 and no exclusion reason applies. Only the first applicable reason is recorded.

| Id | Inclusion |
|:--|:-------------------------------------------------------------|
| I1 | Analog electronic circuit, or the analog part of a mixed-signal circuit |
| I2 | Selects, orders or optimises test points, stimuli, measurements or specification tests; or analyses testability or ambiguity groups; or is an in-field self-test of an analog board that decides what to measure |
| I3 | Primary study with a method applied to at least one circuit |
| I4 | Full text in English or Spanish |

| Id | Exclusion | Typical example |
|:--|:-----------------------------|:------------------------------------|
| E1 | Digital only | Test point insertion in logic, scan chains |
| E2 | Diagnosis without selection: features and a classifier on fixed measurements | "Fault diagnosis with wavelets and a neural network", always measuring the output |
| E3 | Other domain | Power networks, sensor placement in a plant |
| E4 | Test technique, structure or tool (BIST, DfT, simulation, fault models) that does not decide what to measure | A BIST architecture or a fault simulator |
| E5 | Not a primary study (reviews are tagged separately) | Editorial, tutorial, survey |
| E6 | Redundant version: the most complete one is kept | Conference paper later extended in a journal |
| E7 | Language | |
| E8 | Full text not available | |

Boundary cases:

- **Feature selection.** Included if what is selected are frequencies, nodes or sampling instants; excluded by E2 if they are mathematical transformations of a signal already measured.
- **Analog automatic test pattern generation (ATPG).** Included.
- **System-level test selection** (dependency matrices). Included only if the example is an analog circuit.
- **Integrated circuit or board.** Both are in scope.

# 5. Selection

1. Deduplication with a script (DOI and normalised title).
2. Screening by title and abstract, with three possible decisions: include, exclude or doubt. A doubt goes to full text.
3. Full-text screening.
4. PRISMA flow diagram.

An AI assistant makes a first pass of the title and abstract screening, which is stored separately. The decision that counts is the human one, taken with that proposal in view. The agreement between both is reported and the use of AI is declared in the paper.

Screening is done by one reviewer. A sample of the decisions is checked independently by a second reviewer who does not see the first decision; agreement is reported with Cohen's kappa and disagreements are resolved by discussion. A reviewer does not check studies from their own group.

# 6. Data extraction and synthesis

One row per included study, following the classification scheme (separate document). A sample of the extraction is checked independently in the same way as the screening.

The synthesis is descriptive: counts by family, year and level; a matrix of studies against the cross-cutting criteria; the distribution of Monte Carlo sample sizes; and a table of the figures published for the most common benchmark circuits.

# 7. Expected limitations

Screening and extraction by a single reviewer with partial independent checking; IEEE Xplore searched by metadata only; English and Spanish only; no grey literature.

# 8. Data availability

The search log, the deduplicated corpus, the screening decisions with exclusion reasons, the extraction matrix and the notebooks that produce every count will be published in an open repository with a DOI when the paper is submitted.

\newpage

# Appendix A. Search strings

Every record must mention `analog*` or `mixed signal`. The unambiguous terms of the field (first group) require nothing else; the general ones also require a circuit term and a fault term. Searches run on 12 October 2026.

## Scopus (1,380 records)

Advanced document search, no filters.

```text
TITLE-ABS-KEY ( ( analog* OR "mixed signal" ) AND (
  ( ( "test point*" OR "test node*" OR "measurement node*" OR "test frequenc*" ) W/3 ( select* OR optim* OR choos* OR choice OR placement ) )
  OR "ambiguity group*" OR "ambiguity set*" OR "fault dictionar*" OR "test compaction"
  OR (
    ( circuit* OR filter* OR amplifier* OR board* OR "front end" )
    AND ( fault* OR defect* OR diagnos* OR "self test*" OR bist OR "built in" )
    AND (
      ( ( "test point*" OR "test node*" OR "measurement node*" OR "measurement point*" OR "test frequenc*" OR stimul* OR excitation* OR "test signal*" OR "test set*" OR "test vector*" OR "test measurement*" OR "specification test*" )
        W/3 ( select* OR optim* OR choos* OR choice OR placement OR minim* OR reduc* OR compact* OR generat* OR order* ) )
      OR "test selection" OR "test generation" OR "test pattern generation" OR atpg OR "adaptive test*"
      OR testability OR diagnosability
    )
  )
) )
AND ( DOCTYPE ( ar ) OR DOCTYPE ( cp ) OR DOCTYPE ( re ) OR DOCTYPE ( ch ) )
```

## Web of Science Core Collection (801 records)

Advanced Search, all editions. Same string as Scopus with `TS=( … )` and `NEAR/3` in place of `W/3`, and no document type filter.

## IEEE Xplore (545 and 488 records)

Command Search. Xplore limits the number of terms and wildcards, so the string is adapted into two queries.

X1, nodes and testability:

```text
("All Metadata":analog OR "All Metadata":analogue OR "All Metadata":"mixed-signal")
AND ("All Metadata":"test point" OR "All Metadata":"test node" OR "All Metadata":"measurement node" OR "All Metadata":"ambiguity group" OR "All Metadata":testability OR "All Metadata":diagnosability OR "All Metadata":"fault dictionary")
AND ("All Metadata":fault OR "All Metadata":defect OR "All Metadata":diagnosis)
```

X2, stimuli and test sets:

```text
("All Metadata":analog OR "All Metadata":analogue OR "All Metadata":"mixed-signal")
AND ("All Metadata":"test selection" OR "All Metadata":"test compaction" OR "All Metadata":"test generation" OR "All Metadata":"test set" OR "All Metadata":"test stimulus" OR "All Metadata":"test frequency" OR "All Metadata":"adaptive test" OR "All Metadata":"specification test" OR "All Metadata":ATPG)
AND ("All Metadata":fault OR "All Metadata":defect OR "All Metadata":diagnosis)
```

## Author searches

Scopus author identifiers, 2020 onwards: Stratigopoulos; Chatterjee (A.); Sunter; Manetti, Piccirilli, Grasso, Luchetta; Starzyk; Tadeusiewicz, Hałgas; Golonek, Rutkowski, Grzechca; Lubaszewski, Balen; Czaja; and the authors of K10 and K11.

# Appendix B. Control set

| Id | Reference | DOI |
|:--|:--------------------------------------|:------------------------------|
| K01 | Chakrabarti and Chatterjee, ICCAD 2000 | 10.1109/ICCAD.2000.896532 |
| K02 | Huang and Cheng, ITC 1997 | 10.1109/TEST.1997.639675 |
| K03 | Huang and Cheng, TCAS-II 2000 | 10.1109/82.877140 |
| K04 | Tadeusiewicz and Hałgas, JETTA 2017 | 10.1007/s10836-017-5650-4 |
| K05 | Brosa and Figueras, ETW 1999 | 10.1109/ETW.1999.804430 |
| K06 | Zilch, Lubaszewski and Balen, AICSP 2022 | 10.1007/s10470-022-02039-6 |
| K07 | Tang et al., IEEE TCAD 2018 | 10.1109/TCAD.2017.2762647 |
| K08 | Spinks et al., JETTA 2004 | 10.1023/B:JETT.0000009310.48706.b7 |
| K09 | Grzechca, ECCTD 2011 | 10.1109/ECCTD.2011.6043396 |
| K10 | Yang et al., EAAI 2026 | 10.1016/j.engappai.2025.113294 |
| K11 | Liu et al., IEEE TIM 2025 | 10.1109/TIM.2025.3588964 |
| K12 | Ankush et al. (CODA), ETS 2026 | 10.1109/ETS69887.2026.11591724 |
| K13 | Hochwald and Bastian, TCAS 1979 | 10.1109/TCS.1979.1084665 |
| K14 | Lin and Elcherif, IJCTA 1985 | 10.1002/cta.4490130205 |
| K15 | Stenbakken and Souders, IEEE TIM 1987 | |
| K16 | Milor and Sangiovanni-Vincentelli, IEEE TCAD 1994 | 10.1109/43.285252 |
| K17 | Fedi, Manetti, Piccirilli and Starzyk, TCAS-I 1999 | 10.1109/81.774222 |
| K18 | Prasad and Babu, IEEE TIM 2000 | 10.1109/19.893273 |
| K19 | Manetti and Piccirilli, TCAS-I 2003 | 10.1109/TCSI.2003.809811 |
| K20 | Starzyk et al., IEEE TIM 2004 | 10.1109/TIM.2004.827085 |
| K21 | Golonek and Rutkowski, TCAS-II 2007 | 10.1109/TCSII.2006.884112 |
| K22 | Yang, Tian and Long, IEEE TIM 2009 | 10.1109/TIM.2008.2006725 |
| K23 | Biswas, Blanton and Stratigopoulos, DATE 2005 | 10.1109/DATE.2005.277 |
| K24 | Ma et al., Math. Probl. Eng. 2018 | 10.1155/2018/9714206 |
