"""Demonstrates the use of the package.

Gets the current weather.

Usage
-----
> get_weather.py
Fetching locations...
INFO:root:Searching data for time window 2022-02-09T09:47:59...2022-02-10T09:47:59.
INFO:root:Found 1320 entries.
INFO:root:Latest entry at 2022-02-10 07:50:00.
Locations:
    Alajärvi Möksy
    Espoo Tapiola
    Haapavesi Mustikkamäki
...
    Virrat Äijänneva
    Ylivieska lentokenttä
    Ähtäri Inha

> get_weather.py 'Tornio Torppi'
Fetching weather data for location 'Tornio Torppi'...
INFO:root:Searching data for time window 2022-02-09T09:46:06...2022-02-10T09:46:06.
INFO:root:Found 76 entries.
Found weather data for location 'Tornio Torppi'.
Found data keys:
    times
    WS_10MIN
    WD_10MIN
    WG_10MIN
    T
    RH
    TD
    P_SEA
    R_1H
    VIS
    N_MAN
    WAWA
Analyzing data...
Plotting data...
"""
import sys
import logging
import argparse

try:
    import matplotlib.pyplot as plt
    import pandas as pd
except ImportError as e:
    print("ERROR: Extras need to installed in order to run this file.")
    print(e)
    sys.exit(-1)

from epps.weather import get_weather_data, get_locations


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument("location", type=str, nargs='?', default='')
    args = parser.parse_args()

    if args.location == '':
        print("Fetching locations...")
        locations = get_locations()
        if locations is None:
            print("Could not find any locations.")
            sys.exit(-1)

        print("Locations:")
        for location in locations:
            print(f"\t{location}")
        sys.exit(0)

    print(f"Fetching weather data for location '{args.location}'...")
    locations, weather_data = get_weather_data(args.location)

    if weather_data is None:
        print(f"Could not fetch weather data for location '{args.location}'.")
        print("Locations:")
        for location in locations:
            print(f"\t{location}")
        sys.exit(-1)

    print(f"Found weather data for location '{args.location}'.")
    print("Found data keys:")
    for key in weather_data.keys():
        print(f"\t{key}")

    print("Analyzing data...")
    t = weather_data['times']
    d = {key: value['values'] for key, value in weather_data.items() if key != 'times'}
    units = {key: value['unit'] for key, value in weather_data.items() if key != 'times'}
    titles = list(d.keys())
    ylabels = list(units.values())

    df = pd.DataFrame.from_dict(d)
    df.index = pd.DatetimeIndex(t)

    print("Plotting data...")
    n_cols = 2
    n_rows = int(len(df.columns)/n_cols) + (len(df.columns) % n_cols)
    axs = df.plot(
        subplots=True,
        sharex=True,
        figsize=(4*n_cols, 2*n_rows),
        layout=(n_rows, n_cols),
        title=args.location,
        legend=False,
        color='black',
        )

    for row in range(n_rows):
        for col in range(n_cols):
            i = row*n_cols + col
            if i < len(ylabels):
                axs[row, col].set_title(titles[i])
                axs[row, col].set_ylabel(ylabels[i])

    
    plt.tight_layout()
    plt.show()
