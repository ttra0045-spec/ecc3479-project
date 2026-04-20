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

Per-game statistics (clean data):

| Game | Rows | Date min | Date max | Players min | Players max | Players mean | Players SD |
|---|---:|---|---|---:|---:|---:|---:|
| Apex Legends | 36 | 2025-01-28 | 2025-03-04 | 94,512 | 226,225 | 162,393.6 | 37,340.1 |
| Counter-Strike 2 | 36 | 2024-04-23 | 2024-05-28 | 1,263,426 | 1,631,616 | 1,494,634.1 | 79,691.9 |
| Dead by Daylight | 36 | 2023-11-14 | 2023-12-19 | 34,866 | 58,019 | 41,177.9 | 5,391.5 |
| Deep Rock Galactic | 36 | 2024-05-30 | 2024-07-04 | 10,380 | 54,160 | 27,956.4 | 13,540.1 |
| Destiny 2 | 36 | 2024-09-24 | 2024-10-29 | 24,629 | 89,537 | 45,207.7 | 16,533.2 |
| Don't Starve Together | 36 | 2023-04-13 | 2023-05-18 | 29,375 | 115,925 | 65,046.7 | 29,714.5 |
| Helldivers 2 | 36 | 2025-08-19 | 2025-09-23 | 39,817 | 178,795 | 105,813.9 | 40,272.2 |
| No Man's Sky | 36 | 2025-01-15 | 2025-02-19 | 8,195 | 43,695 | 22,691.1 | 11,777.9 |
| Palworld | 36 | 2024-12-09 | 2025-01-13 | 33,821 | 212,817 | 126,708.9 | 69,530.4 |
| PUBG: BATTLEGROUNDS | 36 | 2025-10-22 | 2025-11-26 | 591,321 | 755,104 | 645,912.8 | 33,612.0 |
| Sea of Thieves | 36 | 2024-10-03 | 2024-11-07 | 7,791 | 15,873 | 11,309.9 | 2,165.6 |
| Warframe | 36 | 2025-11-26 | 2025-12-31 | 72,137 | 175,546 | 106,446.7 | 26,356.5 |

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

## Raw Data Summary

### PUBG.csv

|       |          Players |
|:------|-----------------:|
| count |   4841           |
| mean  | 587320           |
| std   | 499207           |
| min   |      1           |
| 25%   | 336046           |
| 50%   | 457976           |
| 75%   | 686010           |
| max   |      3.25725e+06 |

### Counter strike 2.csv

|       |          Players |
|:------|-----------------:|
| count |   6613           |
| mean  | 810696           |
| std   | 453347           |
| min   |    204           |
| 25%   | 546354           |
| 50%   | 772352           |
| 75%   |      1.17926e+06 |
| max   |      1.86253e+06 |

### Dead by Daylight.csv

|       |   Players |
|:------|----------:|
| count |    5246   |
| mean  |   43204   |
| std   |   18635.8 |
| min   |       1   |
| 25%   |   29333.8 |
| 50%   |   43712   |
| 75%   |   54501.5 |
| max   |  120717   |

### Warframe.csv

|       |   Players |
|:------|----------:|
| count |    6246   |
| mean  |   52821.8 |
| std   |   20281.2 |
| min   |       1   |
| 25%   |   40977.8 |
| 50%   |   54008   |
| 75%   |   65162.8 |
| max   |  189837   |

### Sea of Thieves.csv

|       |   Players |
|:------|----------:|
| count |   3668    |
| mean  |  12180.3  |
| std   |   8854.64 |
| min   |    321    |
| 25%   |   6173    |
| 50%   |  10144    |
| 75%   |  15715.5  |
| max   |  66906    |

### Dead rock galactic.csv

|       |   Players |
|:------|----------:|
| count |   4822    |
| mean  |   9681.29 |
| std   |   7040.66 |
| min   |      1    |
| 25%   |   5012    |
| 50%   |   9160    |
| 75%   |  13261    |
| max   |  54160    |

### Destiny 2.csv

|       |   Players |
|:------|----------:|
| count |    3914   |
| mean  |   47368.7 |
| std   |   45956.6 |
| min   |    1199   |
| 25%   |    8788   |
| 50%   |   36313.5 |
| 75%   |   73663.5 |
| max   |  316750   |

### No mans sky.csv

|       |   Players |
|:------|----------:|
| count |   5074    |
| mean  |  10582.1  |
| std   |   9819.44 |
| min   |      1    |
| 25%   |   6182    |
| 50%   |   9292    |
| 75%   |  12446    |
| max   | 212604    |

### Apex Legends.csv

|       |   Players |
|:------|----------:|
| count |      3513 |
| mean  |    205830 |
| std   |    116624 |
| min   |     46958 |
| 25%   |    104442 |
| 50%   |    186027 |
| 75%   |    281136 |
| max   |    624473 |

### Palworld.csv

|       |          Players |
|:------|-----------------:|
| count |   2342           |
| mean  |  54174.7         |
| std   | 147581           |
| min   |  18883           |
| 25%   |  23894.2         |
| 50%   |  31299.5         |
| 75%   |  41318.8         |
| max   |      2.10187e+06 |

### Dont Starve.csv

|       |   Players |
|:------|----------:|
| count |    5615   |
| mean  |   26323.3 |
| std   |   16952.5 |
| min   |    1776   |
| 25%   |   12077.5 |
| 50%   |   21980   |
| 75%   |   38673.5 |
| max   |  115925   |

### Helldivers.csv

|       |   Players |
|:------|----------:|
| count |    2491   |
| mean  |   54542.4 |
| std   |   50552.9 |
| min   |       1   |
| 25%   |   35083.5 |
| 50%   |   47747   |
| 75%   |   57379   |
| max   |  458709   |

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

### Does a first-order effect exist?

Using day index within each 36-day window as a first-order time predictor:

- pooled correlation across all games: $r(\text{day}, \text{players}) = 0.0265$ (near zero)
- pooled with log transform: $r(\text{day}, \log(\text{players})) = 0.1358$ (still weak)
- within-game sign pattern: 10 of 12 games have positive $r(\text{day}, \text{players})$
- pooled after within-game standardization (z-score by game): $r(\text{day}, z_{\text{within game}}) = 0.3455$

Interpretation:

- A first-order effect does exist within many games (player counts often rise through the event window).
- The effect is masked when all games are pooled without adjustment.

Examples of stronger within-game first-order effects:

- Palworld: $r = 0.7850$
- No Man's Sky: $r = 0.7714$
- Don't Starve Together: $r = 0.5978$
- Deep Rock Galactic: $r = 0.5603$
- Warframe: $r = 0.5305$

Near-flat/weak negative examples:

- PUBG: $r = -0.0227$
- Sea of Thieves: $r = -0.1428$

Compact per-game correlation summary:

| Game | $r(\text{day}, \text{players})$ | $r(\text{day}, \log(\text{players}))$ | Direction |
|---|---:|---:|---|
| Apex Legends | 0.5390 | 0.5983 | Positive |
| Counter-Strike 2 | 0.0312 | 0.0369 | Positive (very weak) |
| Dead by Daylight | 0.0270 | 0.0256 | Positive (very weak) |
| Deep Rock Galactic | 0.5603 | 0.6762 | Positive |
| Destiny 2 | 0.4095 | 0.5240 | Positive |
| Don't Starve Together | 0.5978 | 0.6756 | Positive |
| Helldivers 2 | 0.0601 | 0.1994 | Positive (weak) |
| No Man's Sky | 0.7714 | 0.8130 | Positive (strong) |
| Palworld | 0.7850 | 0.8343 | Positive (strong) |
| PUBG: BATTLEGROUNDS | -0.0227 | -0.0094 | Negative (very weak) |
| Sea of Thieves | -0.1428 | -0.1638 | Negative (weak) |
| Warframe | 0.5305 | 0.6039 | Positive |

### Notes for modeling

- The pooled trend remains close to zero while most within-game trends are positive, indicating aggregation masking.
- Detailed bivariate diagnostics and full modeling implications are provided in Section 6.

## 6. Additional Correlational/Bivariate Analysis

To extend the first-order check, I also tested several bivariate relationships using derived features from `DateTime`.

### Pooled (all games combined)

| Pair | Metric | Result | Quick read |
|---|---:|---:|---|
| day index vs players | Pearson $r$ | 0.0265 | Almost no pooled linear trend |
| day index vs players | Spearman $\rho$ | 0.1672 | Weak pooled monotonic increase |
| day index vs $\log(\text{players})$ | Pearson $r$ | 0.1358 | Slightly clearer after transform |
| weekend indicator vs players | Pearson $r$ | 0.0156 | Weekend effect is negligible when pooled |
| post-update indicator vs players | Pearson $r$ | 0.0438 | Weak pooled step-change signal |
| players$_{t-1}$ vs players$_t$ | Pearson $r$ | 0.9981 | Very strong serial dependence |
| game mean vs game SD (12 games) | Pearson $r$ | 0.6938 | Higher-level games tend to be more variable |

### Per-game bivariate summary (selected diagnostics)

| Game | Spearman $\rho$(day, players) | $r$(post-update, players) | Mean(post)/Mean(pre) | Lag-1 autocorr |
|---|---:|---:|---:|---:|
| Apex Legends | 0.5647 | 0.7578 | 1.449 | 0.8869 |
| Counter-Strike 2 | -0.0188 | 0.2658 | 1.029 | 0.6302 |
| Dead by Daylight | -0.0206 | 0.2760 | 1.077 | 0.4003 |
| Deep Rock Galactic | 0.5274 | 0.8878 | 2.856 | 0.8963 |
| Destiny 2 | 0.5755 | 0.7378 | 1.819 | 0.6989 |
| Don't Starve Together | 0.5663 | 0.8252 | 2.428 | 0.9386 |
| Helldivers 2 | 0.0396 | 0.2409 | 1.209 | 0.8637 |
| No Man's Sky | 0.7022 | 0.9073 | 3.279 | 0.9232 |
| Palworld | 0.6901 | 0.9611 | 4.064 | 0.9701 |
| PUBG: BATTLEGROUNDS | 0.0705 | 0.3343 | 1.036 | 0.4230 |
| Sea of Thieves | -0.1423 | 0.1525 | 1.061 | 0.6552 |
| Warframe | 0.5310 | 0.8550 | 1.580 | 0.7607 |

### Key takeaways from bivariate analysis

1. Serial dependence is very strong.
Daily player counts are highly autocorrelated, so iid assumptions are not appropriate.

2. Update effects are heterogeneous.
Some games show large post-update lifts (Palworld $\times 4.064$, No Man's Sky $\times 3.279$), while others are near flat (Counter-Strike 2 $\times 1.029$).

3. Rank-based trends can differ from Pearson trends.
For a few games, Pearson and Spearman disagree in sign/strength, suggesting nonlinearity or outlier influence within the short 36-day window.

4. Scale and variance move together across games.
Since mean and SD are positively correlated across games, raw-scale models will tend to be heteroskedastic.

### Modeling implications from these bivariate findings

- Prefer dynamic/time-series components (lag terms, AR errors, or state-space approaches).
- Use game-level intercepts and slopes (fixed effects with interactions, or hierarchical random effects).
- Model transformed outcomes (for example, $\log(\text{players})$) and/or use robust/heteroskedasticity-consistent inference.
- Include explicit update-event structure (pre/post indicator, event-time slope changes, or piecewise terms).


