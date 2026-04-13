# Week 4 Worksheet Repository: Exploratory Data Analysis

This repository is for the Timothy Tran's ECC3479

How do major game updates affect short-term player engagement trajectories?

## Repository Structure

Basic folder structure:

```text
ecc3479-project/
├── README.md                                         # Project overview and usage instructions
├── requirements.txt                                  # Python dependencies for notebooks/scripts
├── Code/                                             # Analysis notebooks and code assets
│   ├── Dataset manuplation from raw to clean.ipynb   # Cleans raw CSV files into standardized datasets
│   ├── Trend Code.ipynb                              # Builds trend charts and saves output plots
├── data:raw:/ 
│   ├── raw-data-databook.md                          # Definitions and notes for raw fields
│   └── *.csv                                         # Raw player-count time series by game
├── data:clean:/  
│   ├── clean-data-codebook.md                        # Definitions and notes for cleaned fields
│   └── *.csv                                         # Date-filtered standardized datasets
├── outputs:/                                         # Generated charts and analysis outputs
└── src:/                                             # Python source code modules (if used)
```

This repository is organized around a simple analysis pipeline:

1. **Raw data source**
   - [data:raw:](data:raw:): Original CSV files for 12 games (Palworld, Helldivers 2, No Man's Sky, Destiny 2, Counter-Strike 2, Apex Legends, Deep Rock Galactic, Don't Starve Together, Dead by Daylight, PUBG: BATTLEGROUNDS, Sea of Thieves, Warframe).
   - Raw rows contain timestamp and player-count values (DateTime and Players), stored in the original source format.

2. **Data cleaning and preparation**
   - [Code/Dataset manuplation from raw to clean.ipynb](Code/Dataset%20manuplation%20from%20raw%20to%20clean.ipynb): Filters and prepares cleaned datasets, including metadata like update dates.
   - [data:clean:](data:clean:): Cleaned CSV files with standardized columns `DateTime,Players`.
   - Each clean file is date-filtered per game window, with the end date being 14 days after update date.
   - Each dataset is associated with an `update_date` tracking when the game received a major update or patch.

3. **Trend analysis and visualization**
   - [Code/Trend Code.ipynb](Code/Trend%20Code.ipynb): Generates trend plots for all 12 games showing daily players, 7-day moving average, EMA smoothing, linear trend, and update date markers.
   - [outputs:](outputs:): Saved plot images (one per game) with filename pattern `game_name_players_trend.png`.
   - Each plot includes a red dotted vertical line marking the game's update date, helping visualize how major updates correlate with player count changes.

Additional files:
- [README.md](README.md): Project overview and instructions.
- [requirements.txt](requirements.txt): Python dependencies.

## Generate Clean Data From Raw Data

Use this notebook to convert raw files into analysis-ready clean files:

- [Code/Dataset manuplation from raw to clean.ipynb](Code/Dataset%20manuplation%20from%20raw%20to%20clean.ipynb)

Steps:

1. Open [Code/Dataset manuplation from raw to clean.ipynb](Code/Dataset%20manuplation%20from%20raw%20to%20clean.ipynb) in VS Code.
2. Select your Python kernel/environment.
3. Run Cell 1 (the full pipeline cell).
4. Check [data:clean:](data:clean:) for generated files named like:
   - `game_name_startDate_to_endDate.csv`

What this notebook does:

1. Reads source CSV files from [data:raw:](data:raw:).
2. Filters rows by each dataset's configured start/end window.
3. Associates each dataset with an `update_date` field (e.g., "2024-12-23" for Palworld) to track major game updates.
4. Writes clean CSV files to [data:clean:](data:clean:) with standardized columns `DateTime,Players`.
5. The metadata (including update dates) is used by the trend analysis notebook to mark update dates on plots.


## Trend Analysis & Visualization

The [Code/Trend Code.ipynb](Code/Trend%20Code.ipynb) notebook generates comprehensive trend plots for all 12 games. Each plot displays:

- **Daily Players** (blue line with markers): Raw daily player count data
- **7-Day Moving Average** (crimson line): Smoothed trend reducing daily noise
- **7-Day EMA** (purple line): Exponential moving average for responsive trend detection
- **Linear Trend** (dashed green line): Best-fit trend line across the entire period
- **Update Date** (red dotted vertical line): Marks when the game received a major update or patch

The update date line helps correlate player count changes with game updates. If you see a spike or dip in the moving averages near the update date, it indicates the update significantly affected player engagement.

All plots are saved to [outputs:](outputs:) with the naming pattern: `game_name_players_trend.png`

## Analysis Notes

Will be filled with analysis once it is done

## Documentation

- Raw data databook: [data:raw:/raw-data-databook.md](data:raw:/raw-data-databook.md)
- Clean data codebook: [data:clean:/clean-data-codebook.md](data:clean:/clean-data-codebook.md)


