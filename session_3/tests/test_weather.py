import warnings
from epps.weather import get_locations, get_weather_data


def test_weather_module():
    locations = get_locations()
    if locations is None:
        warnings.warn("get_locations() returned None. This is documented "
                      "behavior, when no locations could be fetched. "
                      "Could not test further.")
        return

    assert type(locations) is list
    assert len(locations) > 0

    location = locations[0]
    locations, weather_data = get_weather_data(location)
    assert weather_data is not None, "get_weather_data() did not return any data"   # noqa: E501
    assert location in locations, "get_weather_data() is missing requested location"   # noqa: E501
    assert isinstance(weather_data, dict)
    assert 'times' in weather_data.keys()
    assert len(weather_data.keys()) > 1
