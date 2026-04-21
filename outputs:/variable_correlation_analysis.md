# 5. Exploratory Analysis Of Variable Correlation

## Pooled Correlation (across all games)
- r(day, players) = 0.3455
- r(day, log(players)) = -0.0193
- r(day, z_within_game) = 0.3455

## Within-Game Trends
10 of 12 games have a positive r(day, players) trend.

### Examples of stronger within-game first-order effects:
| Game                                           |   r(day, players) |
|:-----------------------------------------------|------------------:|
| Palworld 2024 12 09 To 2025 01 13              |          0.785048 |
| No Man S Sky 2025 01 15 To 2025 02 19          |          0.771367 |
| Don T Starve Together 2023 04 13 To 2023 05 18 |          0.597799 |
| Deep Rock Galactic 2024 05 30 To 2024 07 04    |          0.560332 |
| Apex Legends 2025 01 28 To 2025 03 04          |          0.539019 |
| Warframe 2025 11 26 To 2025 12 31              |          0.530523 |

### Near-flat/weak examples:
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