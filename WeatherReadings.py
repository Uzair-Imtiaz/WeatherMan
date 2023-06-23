"""
    This module provides a class, `WeatherReadings`, that represents weather readings for a day.

Usage
-----
    from WeatherReadings import WeatherReadings

    # Create an instance of WeatherReadings
    reading = WeatherReadings(data)

    # Access the attributes of the weather readings
    date = reading.date
    temperature = reading.temperature
    dew_point = reading.dew_point
    humidity = reading.humidity
    sea_level_pressure = reading.sea_level_pressure
    visibility = reading.visibility
    wind_speed = reading.wind_speed
    max_gust_speed = reading.max_gust_speed
    precipitation = reading.precipitation
    cloud_cover = reading.cloud_cover
    events = reading.events
    wind_dir_degrees = reading.wind_dir_degrees
"""


class _Temperature:
    """
    A private class to hold max, min and mean temperatures.

    Attributes
    ----------
    max : int
        Maximum value of temperature.

    mean : int
        Minimum value of temperature.

    min : int
    """

    def __init__(self, max_, mean, min_) -> None:
        """
        Constructor

        Arguments
        ---------
        max_ : int
            Maximum value of temperature.

        mean : int
            Mean value of temperature.

        min_ : int
            Minimum value of temperature.
        """

        self.max = int(max_) if max_.isdigit() else 0
        self.mean = int(mean) if mean.isdigit() else 0
        self.min = int(min_) if min_.isdigit() else 0


class _DewPoint:
    """
    A private class to hold std, mean and min dew point.

    Attributes
    ----------
    std : int
        Standard value of dew point.

    mean : int
        Mean value of dew point.

    min : int
        Minimum value of dew point.
    """

    def __init__(self, std, mean, min_) -> None:
        """
        Constructor

        Arguments
        ---------
        std : int
            Standard value of dew point.

        mean : int
            Mean value of dew point.

        min_ : int
            Minimum value of dew point.
        """

        self.std = int(std) if std.isdigit() else 0
        self.mean = int(mean) if mean.isdigit() else 0
        self.min = int(min_) if min_.isdigit() else 0


class _Humidity:
    """
    A private class to hold max, mean and min Humidity.

    Attributes
    ----------
    max : int
        Standard value of humidity.

    mean : int
        Mean value of humidity.

    min : int
        Minimum value of humidity.
    """

    def __init__(self, max_, mean, min_) -> None:
        """
        Constructor

        Arguments
        ---------
        max_ : int
        Standard value of humidity.

        mean : int
            Mean value of humidity.

        min_ : int
            Minimum value of humidity.
        """

        self.max = int(max_) if max_.isdigit() else 0
        self.mean = int(mean) if mean.isdigit() else 0
        self.min = int(min_) if min_.isdigit() else 0


class _SeaLevelPressure:
    """
    A private class to hold max, mean and min Sea level pressure.

    Attributes
    ----------
    max : int
        Standard value of Sea level pressure.

    mean : int
        Mean value of Sea level pressure.

    min : int
        Minimum value of Sea level pressure.
    """

    def __init__(self, max_, mean, min_) -> None:
        """
        Constructor

        Arguments
        ----------
        max_ : int
            Standard value of Sea level pressure.

        mean : int
            Mean value of Sea level pressure.

        min_ : int
            Minimum value of Sea level pressure.
        """

        self.max = int(max_) if max_.isdigit() else 0
        self.mean = int(mean) if mean.isdigit() else 0
        self.min = int(min_) if min_.isdigit() else 0


class _Visibility:
    """
    A private class to hold max, mean and min Visibility.

    Attributes
    ----------
    max : int
        Standard value of Visibility.

    mean : int
        Mean value of Visibility.

    min : int
        Minimum value of Visibility.
    """

    def __init__(self, max_, mean, min_) -> None:
        """
        Constructor.

        Attributes
        ----------
        max_ : int
            Standard value of Visibility.

        mean : int
            Mean value of Visibility.

        min_ : int
            Minimum value of Visibility.
        """

        self.max = int(max_) if max_.isdigit() else 0
        self.mean = int(mean) if mean.isdigit() else 0
        self.min = int(min_) if min_.isdigit() else 0


class _WindSpeed:
    """
    A private class to hold max and mean wind speed.

    Attributes
    ----------
    max : int
        Standard value of Wind speed.

    mean : int
        Mean value of Wind speed.
    """

    def __init__(self, max_, mean) -> None:
        """
        Constructor.

        Arguments
        ----------
        max_ : int
            Standard value of Wind speed.

        mean : int
            Mean value of Wind speed.
        """

        self.max = int(max_) if max_.isdigit() else 0
        self.mean = int(mean) if mean.isdigit() else 0


class WeatherReadings:
    """
    A class to hold weather readings.

    Attributes
    ----------
    date : str
        Date in string format.

    temperature : _Temperature
        Temperature values for a day.

    dew_point : _DewPoint
        Dew Point values for a day.

    humidity : _Humidity
        Humidity values for a day.

    sea_level_pressure : _SeaLevelPressure
        Sea level pressure values for a day.

    visibility : _Visibility
        Visibility values for a day.

    wind_speed : _WindSpeed
        Wind speed values for a day.

    max_gust_speed : str
        Maximum gust speed if available for a day.

    precipitation : str
        Precipitation value if available for a day.

    cloud_cover : str
        Cloud cover value if available for a day.

    events : str
        Events on a given day if available.

    wind_dir_degrees : str
        Direction of wind in degrees.
    """

    def __init__(self, data) -> None:
        """
        Parameterised constructor.

        Arguments
        ---------
        data : list
            A list where each index is a value for a day from the file in sequential order.
        """

        self.date = data[0]
        self.temperature = _Temperature(data[1], data[2], data[3])
        self.dew_point = _DewPoint(data[4], data[5], data[6])
        self.humidity = _Humidity(data[7], data[8], data[9])
        self.sea_level_pressure = _SeaLevelPressure(data[10], data[11], data[12])
        self.visibility = _Visibility(data[13], data[14], data[15])
        self.wind_speed = _WindSpeed(data[16], data[17])
        self.max_gust_speed = data[18]
        self.precipitation = data[19]
        self.cloud_cover = data[20]
        self.events = data[21]
        self.wind_dir_degrees = data[22]
