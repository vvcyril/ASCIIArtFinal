# UK Map ASCII Art Generator

A Python script that generates an ASCII art representation of the UK map using postcode data. 

## Features

- **Dynamic Size Control:** Specify the width and height of the generated map.
- **Customizable Markers:** Choose the character used to represent land areas.
- **Remote Data Handling:** Automatically downloads and caches postcode data (compressed CSV format).
- **Efficient Data Processing:** Processes UK postcode data to generate grid coordinates for mapping.

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies:

```python
pip install -r requirements.txt
```
## Usage
Run the script with optional command-line arguments to customize the output:
```python
python uk_map_generator.py [--width WIDTH] [--height HEIGHT] [--marker MARKER]
```
#### Arguments
-w, --width: Output width in characters (default: 80)

-ht, --height: Output height in characters (default: 24)

-m, --marker: Character to use for land markers (default: "*")

#### Example:
```python
python uk_map_generator.py --width 100 --height 30 --marker *
```
This will generate a UK map with a width of 100 characters, height of 30 characters, and use * as the land marker.

## Data Source
The script uses UK postcode data from GitHub for generating the map. The data is downloaded and cached locally for future use.

Link: [https://github.com/dwyl/uk-postcodes-latitude-longitude-omplete-csv/raw/master/ukpostcodes.csv.zip](https://github.com/dwyl/uk-postcodes-latitude-longitude-complete-csv/tree/master)
