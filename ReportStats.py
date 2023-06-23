"""
    This module provides a class, `ReportStats`, that holds the calculation results for the reports.

Usage
-----
    from ReportStats import ReportStats

    # Create an instance of ReportStats
    report_stats = ReportStats()

    # Set the extreme values and their corresponding dates
    report_stats.set_extremes(highest, day_of_highest, lowest, day_of_lowest, humidity, most_humid_day)

    # Set the average values
    report_stats.set_averages(highest_avg_temperature, lowest_avg_temperature, avg_mean_humidity)
"""


class ReportStats:
    """
    A class that will hold the calculations results.

    Attributes
    ----------
    average_of_mean_humidity : int >= 0
        Holds the average of the mean humidity of the month.

    lowest_average_temperature : int >= 0
        Holds the minimum of the average temperatures from the readings of the month.

    highest_average_temperature : int >= 0
        Holds the maximum of the average temperatures from the readings of the month.

    humidity : int >= 0
        Holds the value of the maximum humidity of the month.

    lowest_temperature_day : str
        Date when the lowest temperature was recorded in string format.

    lowest_temperature : int >= 0
        Holds the minimum temperature value of the month.

    highest_temperature_day : str
        Date when the highest temperature was recorded in string format.

    highest_temperature : int >= 0
         Holds the maximum temperature value of the month.

    most_humid_day : str
        Date when the most humidity was recorded in string format.

    Methods
    -------
    set_extremes
        Assign the extreme(highest, lowest) values of temperature and humidity and record the date when it occurred.

    set_average
        Assign the average values of highest and lowest temperature and humidity.
    """

    def __init__(self):
        """
        Constructor

        Initialise the attributes by none values.
        """

        self.average_of_mean_humidity = None
        self.lowest_average_temperature = None
        self.highest_average_temperature = None
        self.humidity = None
        self.lowest_temperature_day = None
        self.lowest_temperature = None
        self.highest_temperature_day = None
        self.highest_temperature = None
        self.most_humid_day = None

    def set_extremes(self, highest, day_of_highest, lowest, day_of_lowest, humidity, most_humid_day) -> None:
        """
        Assign the extreme(highest, lowest) values of temperature and humidity and record the date when it occurred.

        Parameters
        ----------
        highest : int
            The highest temperature recorded in a month.

        day_of_highest : str
            Date when the highest temperature was recorded in string format.

        lowest : int
            The lowest temperature recorded in a month.

        day_of_lowest : str
            Date when the lowest temperature was recorded in string format.

        humidity : int
            The maximum value of humidity recorded in a month.

        most_humid_day : str
            Date when the maximum humidity was recorded in string format.
        """

        self.highest_temperature = highest
        self.highest_temperature_day = day_of_highest
        self.lowest_temperature = lowest
        self.lowest_temperature_day = day_of_lowest
        self.humidity = humidity
        self.most_humid_day = most_humid_day

    def set_averages(self, highest_avg_temperature, lowest_avg_temperature, avg_mean_humidity) -> None:
        """
        Assign the average values of highest and lowest temperature and humidity.

        Parameters
        ----------
        highest_avg_temperature : int
            The average of the highest temperature of the month.

        lowest_avg_temperature : int
            The average of the lowest temperature of the month.

        avg_mean_humidity : int
            The average of the mean humidity of the month.
        """

        self.highest_average_temperature = highest_avg_temperature
        self.lowest_average_temperature = lowest_avg_temperature
        self.average_of_mean_humidity = avg_mean_humidity
