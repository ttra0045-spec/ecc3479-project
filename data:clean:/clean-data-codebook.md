# Clean Data Codebook

## Purpose
This codebook documents the cleaned CSV files in [data:clean:](data:clean:).
It summarizes schema, filename conventions, date-window logic, and file-level coverage.

## How Clean Data Is Produced
Clean files are generated from raw source files by filtering each game to a configured start date and end date window.
The configured end date is extended by 7 days before export, and boundaries are inclusive.
Each dataset has an associated `update_date` that tracks when the game received its last major update or patch, providing context for trend analysis.

## Shared Schema
All clean files use the same two-column structure:

- DateTime (string): Daily timestamp in format YYYY-MM-DD HH:MM:SS
- Players (integer): Daily player count for that date

## Filename Convention
Each cleaned file follows this naming format:

- game_name_startDate_to_endDate.csv

Where:

- game_name is lowercased and sanitized with underscores
- startDate is the configured start date
- endDate is the extended end date (original end plus 7 days)

## Data Dictionary

| Dataset file | Rows | Date min | Date max | Update Date |
|---|---:|---|---|---|
| apex_legends_2025-01-28_to_2025-03-04.csv | 36 | 2025-01-28 | 2025-03-04 | 2025-02-11 |
| counter_strike_2_2024-04-23_to_2024-05-28.csv | 36 | 2024-04-23 | 2024-05-28 | 2024-05-07 |
| dead_by_daylight_2023-11-14_to_2023-12-19.csv | 36 | 2023-11-14 | 2023-12-19 | 2023-11-28 |
| deep_rock_galactic_2024-05-30_to_2024-07-04.csv | 36 | 2024-05-30 | 2024-07-04 | 2024-06-13 |
| destiny_2_2024-09-24_to_2024-10-29.csv | 36 | 2024-09-24 | 2024-10-29 | 2024-10-08 |
| don_t_starve_together_2023-04-13_to_2023-05-18.csv | 36 | 2023-04-13 | 2023-05-18 | 2023-04-27 |
| helldivers_2_2025-08-19_to_2025-09-23.csv | 36 | 2025-08-19 | 2025-09-23 | 2025-09-02 |
| no_man_s_sky_2025-01-15_to_2025-02-19.csv | 36 | 2025-01-15 | 2025-02-19 | 2025-01-29 |
| palworld_2024-12-09_to_2025-01-13.csv | 36 | 2024-12-09 | 2025-01-13 | 2024-12-23 |
| pubg__battlegrounds_2025-10-22_to_2025-11-26.csv | 36 | 2025-10-22 | 2025-11-26 | 2025-11-05 |
| sea_of_thieves_2024-10-03_to_2024-11-07.csv | 36 | 2024-10-03 | 2024-11-07 | 2024-10-17 |
| warframe_2025-11-26_to_2025-12-31.csv | 36 | 2025-11-26 | 2025-12-31 | 2025-12-10 |

## Usage Notes
- Parse DateTime as datetime before plotting or modeling.
- Sort by DateTime ascending before computing rolling or exponential averages.
- Keep these clean files as analysis-ready extracts; regenerate from the notebook if window definitions change.
