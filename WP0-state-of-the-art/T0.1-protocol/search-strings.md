---
title: "Search strings"
subtitle: "The queries of blocks S1 and S2 in each database, and the author searches"
author: "Telmo Miguel-Medina"
date: today
doctype: "Protocol annex"
reference: "WP0 · T0.1"
---

# Summary {-}

Block S1 (test design) has been run: 3214 records before deduplication. Block S2 (safety coverage) is to be run in T0.2. The counts and the check of the control set ([control_set.csv](control_set.csv)) are in the notebook of `T0.2-search-and-deduplication`: K01–K24 check S1 and K25–K27 check S2.

# S1 · Test design

Every record must mention `analog*` or `mixed signal`. The unambiguous terms of the field (first group) require nothing else; the general ones also require a circuit term and a fault term.

## Scopus (1380 records)

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

Advanced Search, "Query Preview" box, all editions.

```text
TS=( ( analog* OR "mixed signal" ) AND (
  ( ( "test point*" OR "test node*" OR "measurement node*" OR "test frequenc*" ) NEAR/3 ( select* OR optim* OR choos* OR choice OR placement ) )
  OR "ambiguity group*" OR "ambiguity set*" OR "fault dictionar*" OR "test compaction"
  OR (
    ( circuit* OR filter* OR amplifier* OR board* OR "front end" )
    AND ( fault* OR defect* OR diagnos* OR "self test*" OR bist OR "built in" )
    AND (
      ( ( "test point*" OR "test node*" OR "measurement node*" OR "measurement point*" OR "test frequenc*" OR stimul* OR excitation* OR "test signal*" OR "test set*" OR "test vector*" OR "test measurement*" OR "specification test*" )
        NEAR/3 ( select* OR optim* OR choos* OR choice OR placement OR minim* OR reduc* OR compact* OR generat* OR order* ) )
      OR "test selection" OR "test generation" OR "test pattern generation" OR atpg OR "adaptive test*"
      OR testability OR diagnosability
    )
  )
) )
```

## IEEE Xplore (545 and 488 records)

Command Search. Xplore limits terms and wildcards, so the string is adapted into two queries.

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

# S2 · Safety coverage

Every record must mention an analog circuit or measurement chain. The metrics of the standards and FMEDA require nothing else; the general safety terms also require a coverage, fault injection or self-test term. If S2 gives more than 1500 new records after deduplication against S1, `diagnos*` is removed from the last group and the search is repeated.

## Scopus

```text
TITLE-ABS-KEY ( ( analog* OR "mixed signal" OR "signal chain" OR "measurement chain" OR "sensor interface" OR "battery management" ) AND (
  "diagnostic coverage" OR "safe failure fraction" OR "single point fault metric" OR "latent fault metric"
  OR fmeda OR "failure modes effects and diagnostic*"
  OR (
    ( "functional safety" OR "ISO 26262" OR "IEC 61508" OR "IEC 60601" OR "IEEE 2427" OR "P2427" OR "safety mechanism*" OR asil OR "safety integrity level" )
    AND ( "fault coverage" OR "defect coverage" OR "fault injection" OR "fault simulation" OR "defect simulation" OR "self test*" OR bist OR "built in test" OR diagnos* )
  )
) )
AND ( DOCTYPE ( ar ) OR DOCTYPE ( cp ) OR DOCTYPE ( re ) OR DOCTYPE ( ch ) )
```

## Web of Science Core Collection

```text
TS=( ( analog* OR "mixed signal" OR "signal chain" OR "measurement chain" OR "sensor interface" OR "battery management" ) AND (
  "diagnostic coverage" OR "safe failure fraction" OR "single point fault metric" OR "latent fault metric"
  OR fmeda OR "failure modes effects and diagnostic*"
  OR (
    ( "functional safety" OR "ISO 26262" OR "IEC 61508" OR "IEC 60601" OR "IEEE 2427" OR "P2427" OR "safety mechanism*" OR asil OR "safety integrity level" )
    AND ( "fault coverage" OR "defect coverage" OR "fault injection" OR "fault simulation" OR "defect simulation" OR "self test*" OR bist OR "built in test" OR diagnos* )
  )
) )
```

## IEEE Xplore

X3, metrics of the standards:

```text
("All Metadata":analog OR "All Metadata":"mixed-signal" OR "All Metadata":"battery management")
AND ("All Metadata":"diagnostic coverage" OR "All Metadata":"safe failure fraction" OR "All Metadata":"single point fault metric" OR "All Metadata":"latent fault metric" OR "All Metadata":FMEDA)
```

X4, safety and coverage:

```text
("All Metadata":analog OR "All Metadata":"mixed-signal")
AND ("All Metadata":"functional safety" OR "All Metadata":"ISO 26262" OR "All Metadata":"IEC 61508" OR "All Metadata":"safety mechanism" OR "All Metadata":ASIL)
AND ("All Metadata":"fault coverage" OR "All Metadata":"defect coverage" OR "All Metadata":"fault injection" OR "All Metadata":"fault simulation" OR "All Metadata":"self-test" OR "All Metadata":BIST)
```

# Author searches (T0.4)

From 2020 onwards: Stratigopoulos; Chatterjee (A.); Sunter; Manetti, Piccirilli, Grasso, Luchetta; Starzyk; Tadeusiewicz, Hałgas; Golonek, Rutkowski, Grzechca; Lubaszewski, Balen; Czaja; Fummi; and the authors of K10 and K11.
