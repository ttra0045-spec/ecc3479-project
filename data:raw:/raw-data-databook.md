# Raw Data Databook

## Purpose
This databook documents the raw CSV files in `data:raw:`.
It summarizes structure, date coverage, completeness, and basic value ranges.

## Shared Schema
All raw files use the same two-column structure:

- `DateTime` (string): Daily timestamp in format `YYYY-MM-DD HH:MM:SS`
- `Players` (integer-like): Daily peak/concurrent player count

## Data Dictionary

| Dataset file | Rows | Date min | Date max | Missing DateTime | Missing Players | Players min | Players max |
|---|---:|---|---|---:|---:|---:|---:|
| Apex Legends.csv | 3513 | 2020-11-05 | 2026-03-30 | 0 | 0 | 46958 | 624473 |
| Counter strike 2.csv | 6776 | 2011-11-30 | 2026-03-30 | 0 | 163 | 204 | 1862531 |
| Dead by Daylight.csv | 5249 | 2016-02-04 | 2026-03-30 | 0 | 3 | 1 | 120717 |
| Dead rock galactic.csv | 4949 | 2016-12-01 | 2026-03-30 | 0 | 127 | 1 | 54160 |
| Destiny 2.csv | 3914 | 2019-10-01 | 2026-03-30 | 0 | 0 | 1199 | 316750 |
| Dont Starve.csv | 5679 | 2014-12-01 | 2026-03-30 | 0 | 64 | 1776 | 115925 |
| Helldivers.csv | 4692 | 2017-08-14 | 2026-03-30 | 0 | 2201 | 1 | 458709 |
| No mans sky.csv | 5291 | 2015-12-24 | 2026-03-30 | 0 | 217 | 1 | 212604 |
| PUBG.csv | 4886 | 2017-02-01 | 2026-03-30 | 0 | 45 | 1 | 3257248 |
| Palworld.csv | 2342 | 2024-01-19 | 2026-03-30 | 0 | 0 | 18883 | 2101867 |
| Sea of Thieves.csv | 3668 | 2020-06-03 | 2026-03-30 | 0 | 0 | 321 | 66906 |
| Warframe.csv | 6348 | 2013-02-01 | 2026-03-30 | 0 | 102 | 1 | 189837 |

## Data Quality Notes

- `DateTime` has no missing values across all files.
- Several files have missing `Players` values and should be cleaned before modeling.
- `Helldivers.csv` has the largest `Players` missingness (2201 rows).
- Some datasets include very low values (`Players = 1`), which may represent true low activity or placeholders.

## Suggested Cleaning Rules

- Parse `DateTime` as datetime and sort ascending before analysis.
- Convert `Players` to numeric and coerce errors to missing.
- For date-range extraction tasks, use inclusive boundaries.
- Keep raw files unchanged and write transformed files into `data:clean:`.
