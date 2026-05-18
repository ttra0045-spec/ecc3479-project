# 5. Exploratory Analysis Of Variable Correlation

## Pooled Correlation (across all games)
- r(day, players) = 0.0565
- r(day, log(players)) = 0.1900
- r(day, z_within_game) = 0.3402

## Within-Game Trends
13 of 16 games have a positive r(day, players) trend.

### Examples of stronger within-game first-order effects:
| Game                                           |   r(day, players) |
|:-----------------------------------------------|------------------:|
| Palworld 2024 12 09 To 2025 01 13              |          0.785048 |
| No Man S Sky 2025 01 15 To 2025 02 19          |          0.771367 |
| V Rising 2025 04 21 To 2025 05 19              |          0.61451  |
| Don T Starve Together 2023 04 13 To 2023 05 18 |          0.597799 |
| Deep Rock Galactic 2024 05 30 To 2024 07 04    |          0.560332 |
| Apex Legends 2025 01 28 To 2025 03 04          |          0.539019 |
| Warframe 2025 11 26 To 2025 12 31              |          0.530523 |
| Rainbow Six Siege 2024 08 19 To 2024 09 16     |          0.530401 |

### Near-flat/weak examples:
| Game                                         |   r(day, players) |
|:---------------------------------------------|------------------:|
| The Finals 2024 12 05 To 2025 01 02          |        -0.184846  |
| Sea Of Thieves 2024 10 03 To 2024 11 07      |        -0.14275   |
| Pubg  Battlegrounds 2025 10 22 To 2025 11 26 |        -0.0227268 |
| Dead By Daylight 2023 11 14 To 2023 12 19    |         0.0269992 |
| Counter Strike 2 2024 04 23 To 2024 05 28    |         0.03115   |
| Helldivers 2 2025 08 19 To 2025 09 23        |         0.0600944 |

## Compact per-game correlation summary:
| Game                                           |   r(day, players) |   r(day, log(players)) | Direction   |
|:-----------------------------------------------|------------------:|-----------------------:|:------------|
| Apex Legends 2025 01 28 To 2025 03 04          |         0.539019  |             0.59827    | Positive    |
| Counter Strike 2 2024 04 23 To 2024 05 28      |         0.03115   |             0.0368844  | Flat        |
| Dead By Daylight 2023 11 14 To 2023 12 19      |         0.0269992 |             0.0256017  | Flat        |
| Deep Rock Galactic 2024 05 30 To 2024 07 04    |         0.560332  |             0.676182   | Positive    |
| Destiny 2 2024 09 24 To 2024 10 29             |         0.409454  |             0.523974   | Positive    |
| Don T Starve Together 2023 04 13 To 2023 05 18 |         0.597799  |             0.675606   | Positive    |
| Helldivers 2 2025 08 19 To 2025 09 23          |         0.0600944 |             0.199449   | Flat        |
| No Man S Sky 2025 01 15 To 2025 02 19          |         0.771367  |             0.813016   | Positive    |
| Palworld 2024 12 09 To 2025 01 13              |         0.785048  |             0.83434    | Positive    |
| Path Of Exile 2025 06 06 To 2025 07 04         |         0.645881  |             0.807195   | Positive    |
| Pubg  Battlegrounds 2025 10 22 To 2025 11 26   |        -0.0227268 |            -0.00940796 | Flat        |
| Rainbow Six Siege 2024 08 19 To 2024 09 16     |         0.500692  |             0.492598   | Positive    |
| Sea Of Thieves 2024 10 03 To 2024 11 07        |        -0.14275   |            -0.163793   | Negative    |
| The Finals 2024 12 05 To 2025 01 02            |        -0.122757  |            -0.123146   | Negative    |
| V Rising 2025 04 21 To 2025 05 19              |         0.763775  |             0.822966   | Positive    |
| Warframe 2025 11 26 To 2025 12 31              |         0.530523  |             0.603948   | Positive    |