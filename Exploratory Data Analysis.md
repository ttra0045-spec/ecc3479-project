# Basic Description Of Data Characteristics

## 1. What do the variables look like?

All cleaned datasets have the same schema:

- `DateTime` (string datetime, format `YYYY-MM-DD HH:MM:SS`)
- `Players` (integer daily player count)

Example rows from a cleaned file:

| DateTime | Players |
|---|---:|
| 2024-12-09 00:00:00 | 35888 |
| 2024-12-10 00:00:00 | 35637 |
| 2025-01-13 00:00:00 | 138175 |

Across all 12 cleaned files:

- 36 rows per game (daily observations)
- no missing values in either column
- no duplicate dates
- no gaps in daily sequence


## 2. Is this what I would expect?

Yes. For a daily time-series gaming dataset, this is what we want:

- one timestamp per day
- one numeric engagement variable (`Players`)
- consistent variable names across games

The large differences in player counts are also expected by game popularity.
For example, cleaned ranges include:

- lower-volume titles: Sea of Thieves (`7,791` to `15,873`)
- very high-volume titles: Counter-Strike 2 (`1,263,426` to `1,631,616`)

## 3. Anything of particular note?

- Time windows are perfectly standardized (36-day window for every game), which makes cross-game comparisons fair.
- The data contain clear scale differences between games, so comparing absolute counts directly can be misleading unless normalized.
- Date ranges are internally consistent and sorted, which supports moving average/EMA/trend calculations without extra repair steps.

## Clean Data Summary

### deep_rock_galactic_2024-05-30_to_2024-07-04.csv

|       |     Players |
|:------|------------:|
| count | 36          |
| mean  |  1.1719e-16 |
| std   |  1          |
| min   | -1.2981     |
| 25%   | -1.09363    |
| 50%   |  0.142661   |
| 75%   |  0.813115   |
| max   |  1.93527    |

### palworld_2024-12-09_to_2025-01-13.csv

|       |      Players |
|:------|-------------:|
| count | 36           |
| mean  | -2.00457e-17 |
| std   |  1           |
| min   | -1.33593     |
| 25%   | -1.14975     |
| 50%   |  0.3916      |
| 75%   |  0.905519    |
| max   |  1.23842     |

### warframe_2025-11-26_to_2025-12-31.csv

|       |      Players |
|:------|-------------:|
| count | 36           |
| mean  | -1.69617e-16 |
| std   |  1           |
| min   | -1.30175     |
| 25%   | -0.988377    |
| 50%   |  0.185564    |
| 75%   |  0.640423    |
| max   |  2.62172     |

### no_man_s_sky_2025-01-15_to_2025-02-19.csv

|       |      Players |
|:------|-------------:|
| count | 36           |
| mean  |  6.96299e-17 |
| std   |  1           |
| min   | -1.23078     |
| 25%   | -1.10236     |
| 50%   |  0.274237    |
| 75%   |  0.780437    |
| max   |  1.78333     |

### dead_by_daylight_2023-11-14_to_2023-12-19.csv

|       |      Players |
|:------|-------------:|
| count | 36           |
| mean  |  4.37921e-16 |
| std   |  1           |
| min   | -1.17071     |
| 25%   | -0.826002    |
| 50%   | -0.367505    |
| 75%   |  0.606893    |
| max   |  3.12362     |

### don_t_starve_together_2023-04-13_to_2023-05-18.csv

|       |      Players |
|:------|-------------:|
| count | 36           |
| mean  | -2.46716e-17 |
| std   |  1           |
| min   | -1.20048     |
| 25%   | -0.9905      |
| 50%   | -0.0628042   |
| 75%   |  0.853382    |
| max   |  1.71224     |

### pubg__battlegrounds_2025-10-22_to_2025-11-26.csv

|       |      Players |
|:------|-------------:|
| count | 36           |
| mean  |  1.53272e-15 |
| std   |  1           |
| min   | -1.62417     |
| 25%   | -0.784691    |
| 50%   | -0.0870017   |
| 75%   |  0.549861    |
| max   |  3.24857     |

### counter_strike_2_2024-04-23_to_2024-05-28.csv

|       |      Players |
|:------|-------------:|
| count | 36           |
| mean  |  1.28485e-15 |
| std   |  1           |
| min   | -2.90128     |
| 25%   | -0.298153    |
| 50%   |  0.0943871   |
| 75%   |  0.726396    |
| max   |  1.71889     |

### destiny_2_2024-09-24_to_2024-10-29.csv

|       |      Players |
|:------|-------------:|
| count | 36           |
| mean  |  2.22045e-16 |
| std   |  1           |
| min   | -1.24469     |
| 25%   | -0.828074    |
| 50%   | -0.221295    |
| 75%   |  0.532203    |
| max   |  2.68123     |

### sea_of_thieves_2024-10-03_to_2024-11-07.csv

|       |      Players |
|:------|-------------:|
| count | 36           |
| mean  |  2.89892e-16 |
| std   |  1           |
| min   | -1.62489     |
| 25%   | -0.871763    |
| 50%   |  0.0279749   |
| 75%   |  0.823701    |
| max   |  2.10705     |

### apex_legends_2025-01-28_to_2025-03-04.csv

|       |      Players |
|:------|-------------:|
| count | 36           |
| mean  |  3.45403e-16 |
| std   |  1           |
| min   | -1.81793     |
| 25%   | -0.577238    |
| 50%   | -0.0596044   |
| 75%   |  0.883168    |
| max   |  1.70946     |

### helldivers_2_2025-08-19_to_2025-09-23.csv

|       |      Players |
|:------|-------------:|
| count | 36           |
| mean  |  2.46716e-17 |
| std   |  1           |
| min   | -1.63877     |
| 25%   | -0.721233    |
| 50%   |  0.0849877   |
| 75%   |  0.779165    |
| max   |  1.8122      |

## 4. Did data cleaning do anything?

Yes, the cleaning step made meaningful structural changes:

- standardized schema to exactly `DateTime,Players` for all files
- removed quoted header style from raw files and harmonized formatting
- filtered each game to a common analysis window around configured update periods
- produced analysis-ready daily slices with complete, contiguous dates

Impact in size:

- raw total rows: `57,307`
- clean total rows: `432`
- retained after windowing: about `0.75%`

So cleaning did not just tidy names; it intentionally transformed large raw histories into focused, comparable event windows for EDA and trend analysis.

## 5. Exploratory Analysis Of Variable Correlation

### Pooled Correlation (across all games)
- r(day, players) = 0.3455
- r(day, log(players)) = -0.0193
- r(day, z_within_game) = 0.3455

### Within-Game Trends
10 of 12 games have a positive r(day, players) trend.

#### Examples of stronger within-game first-order effects:
| Game                                           |   r(day, players) |
|:-----------------------------------------------|------------------:|
| Palworld 2024 12 09 To 2025 01 13              |          0.785048 |
| No Man S Sky 2025 01 15 To 2025 02 19          |          0.771367 |
| Don T Starve Together 2023 04 13 To 2023 05 18 |          0.597799 |
| Deep Rock Galactic 2024 05 30 To 2024 07 04    |          0.560332 |
| Apex Legends 2025 01 28 To 2025 03 04          |          0.539019 |
| Warframe 2025 11 26 To 2025 12 31              |          0.530523 |

#### Near-flat/weak examples:
| Game                                         |   r(day, players) |
|:---------------------------------------------|------------------:|
| Sea Of Thieves 2024 10 03 To 2024 11 07      |        -0.14275   |
| Pubg  Battlegrounds 2025 10 22 To 2025 11 26 |        -0.0227268 |
| Dead By Daylight 2023 11 14 To 2023 12 19    |         0.0269992 |
| Counter Strike 2 2024 04 23 To 2024 05 28    |         0.03115   |
| Helldivers 2 2025 08 19 To 2025 09 23        |         0.0600944 |

## Compact per-game correlation summary:
| Game                                           |   r(day, players) |   r(day, log(players)) | Direction   |
|:-----------------------------------------------|------------------:|-----------------------:|:------------|
| Apex Legends 2025 01 28 To 2025 03 04          |         0.539019  |            -0.00160659 | Positive    |
| Counter Strike 2 2024 04 23 To 2024 05 28      |         0.03115   |             0.010747   | Flat        |
| Dead By Daylight 2023 11 14 To 2023 12 19      |         0.0269992 |            -0.0518734  | Flat        |
| Deep Rock Galactic 2024 05 30 To 2024 07 04    |         0.560332  |            -0.024988   | Positive    |
| Destiny 2 2024 09 24 To 2024 10 29             |         0.409454  |            -0.0291612  | Positive    |
| Don T Starve Together 2023 04 13 To 2023 05 18 |         0.597799  |             0.146589   | Positive    |
| Helldivers 2 2025 08 19 To 2025 09 23          |         0.0600944 |            -0.0973795  | Flat        |
| No Man S Sky 2025 01 15 To 2025 02 19          |         0.771367  |             0.226869   | Positive    |
| Palworld 2024 12 09 To 2025 01 13              |         0.785048  |             0.212217   | Positive    |
| Pubg  Battlegrounds 2025 10 22 To 2025 11 26   |        -0.0227268 |            -0.229322   | Flat        |
| Sea Of Thieves 2024 10 03 To 2024 11 07        |        -0.14275   |            -0.0136688  | Negative    |
| Warframe 2025 11 26 To 2025 12 31              |         0.530523  |            -0.0741743  | Positive    |

### Notes for modeling

- The pooled trend remains close to zero while most within-game trends are positive, indicating aggregation masking.
- Detailed bivariate diagnostics and full modeling implications are provided in Section 6.


### Key takeaways from bivariate analysis

1. Serial dependence is very strong.
Daily player counts are highly autocorrelated, so iid assumptions are not appropriate.

2. Update effects are heterogeneous.
Some games show large post-update lifts (Palworld $\times 4.064$, No Man's Sky $\times 3.279$), while others are near flat (Counter-Strike 2 $\times 1.029$).

4. Scale and variance move together across games.
Since mean and SD are positively correlated across games, raw-scale models will tend to be heteroskedastic.

### Modeling implications from these bivariate findings

- Prefer dynamic/time-series components (lag terms, AR errors, or state-space approaches).
- Use game-level intercepts and slopes (fixed effects with interactions, or hierarchical random effects).
- Model transformed outcomes (for example, $\log(\text{players})$) and/or use robust/heteroskedasticity-consistent inference.
- Include explicit update-event structure (pre/post indicator, event-time slope changes, or piecewise terms).

## First-Order Analysis Summary

This table summarizes the player count data for each game, showing the mean, standard deviation, min, and max of the z-scored player counts over the observed period. It also includes the first-order correlation between the day and the player count, which indicates the overall trend.

| Game                                           |   Mean Players (Z-score) |   Std Dev Players |   Min Players |   Max Players |   r(day, players) |
|:-----------------------------------------------|-------------------------:|------------------:|--------------:|--------------:|------------------:|
| Apex Legends 2025 01 28 To 2025 03 04          |              3.45403e-16 |                 1 |      -1.81793 |       1.70946 |         0.539019  |
| Counter Strike 2 2024 04 23 To 2024 05 28      |              1.28485e-15 |                 1 |      -2.90128 |       1.71889 |         0.03115   |
| Dead By Daylight 2023 11 14 To 2023 12 19      |              4.37921e-16 |                 1 |      -1.17071 |       3.12362 |         0.0269992 |
| Deep Rock Galactic 2024 05 30 To 2024 07 04    |              1.1719e-16  |                 1 |      -1.2981  |       1.93527 |         0.560332  |
| Destiny 2 2024 09 24 To 2024 10 29             |              2.22045e-16 |                 1 |      -1.24469 |       2.68123 |         0.409454  |
| Don T Starve Together 2023 04 13 To 2023 05 18 |             -2.46716e-17 |                 1 |      -1.20048 |       1.71224 |         0.597799  |
| Helldivers 2 2025 08 19 To 2025 09 23          |              2.46716e-17 |                 1 |      -1.63877 |       1.8122  |         0.0600944 |
| No Man S Sky 2025 01 15 To 2025 02 19          |              6.96299e-17 |                 1 |      -1.23078 |       1.78333 |         0.771367  |
| Palworld 2024 12 09 To 2025 01 13              |             -2.00457e-17 |                 1 |      -1.33593 |       1.23842 |         0.785048  |
| Pubg  Battlegrounds 2025 10 22 To 2025 11 26   |              1.53272e-15 |                 1 |      -1.62417 |       3.24857 |        -0.0227268 |
| Sea Of Thieves 2024 10 03 To 2024 11 07        |              2.89892e-16 |                 1 |      -1.62489 |       2.10705 |        -0.14275   |
| Warframe 2025 11 26 To 2025 12 31              |             -1.69617e-16 |                 1 |      -1.30175 |       2.62172 |         0.530523  |


