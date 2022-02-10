from typing import Tuple, Optional
from datetime import datetime, timedelta
import logging

from fmiopendata.wfs import download_stored_query


def get_locations() -> Optional[list]:
    now = datetime.now().replace(microsecond=0)
    previously = now-timedelta(days=1)
    logging.info(f"Searching data for time window {previously.isoformat()}...{now.isoformat()}.")   # noqa: E501

    model_data = download_stored_query(
        "fmi::observations::weather::cities::multipointcoverage",
        args=[
            f"starttime={previously.isoformat()}",
            f"endtime={now.isoformat()}",
            "bbox=25,60,25.5,60.5",
        ]
    )
    logging.info(f"Found {len(model_data.data)} entries.")
    if len(model_data.data) == 0:
        logging.error("Did not find any entries.")
        return None

    latest_tstep = max(model_data.data.keys())
    logging.info(f"Latest entry at {latest_tstep}.")

    locations = set()
    for data in model_data.data.values():
        for entry in data.keys():
            locations.add(entry)

    return sorted(list(locations))


def get_weather_data(location: str) -> Tuple[list, Optional[dict]]:

    now = datetime.now().replace(microsecond=0)
    yesterday = now-timedelta(days=1)
    logging.info(f"Searching data for time window {yesterday.isoformat()}...{now.isoformat()}.")   # noqa: E501

    model_data = download_stored_query(
        "fmi::observations::weather::cities::multipointcoverage",
        args=[
            f"starttime={yesterday.isoformat()}",
            f"endtime={now.isoformat()}",
            "bbox=25,60,25.5,60.5",
            "timeseries=True",
            f"place={location}"
        ]
    )
    logging.info(f"Found {len(model_data.data)} entries.")

    if location not in model_data.data.keys():
        logging.error(f"Location '{location}' was not found in the fetched data.")   # noqa: E501
        return model_data.data.keys(), None

    return list(model_data.data.keys()), model_data.data[location]
