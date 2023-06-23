"""
    This module provides a class, `ComputeResults`, for computing results for the reports.

Usage
-----
    from ComputeResults import ComputeResults

    # Create an instance of ComputeResults
    compute_results = ComputeResults()

    # Assign the results to a ReportStats object
    results = compute_results.assign_results(weather_readings)
"""

from ReportStats import ReportStats


class ComputeResults:
    """
    A class that will compute the results for the reports and store those in the calculationResults type object.

    Methods
    -------
    assign_to_results_class
        Calculates the weather reading values and assigns them to a CalculationResult type object.
    """

    def __init__(self) -> None:
        pass

    def assign_results(self, weather_readings) -> ReportStats:
        """
        Calculate the values required for the reports and assign them to the CalculationsResult object.

        Parameters
        ----------
        weather_readings : list
            A list of weather reading values of a month.

        Returns
        -------
        calculations : CalculationsResult
            A CalculationsResult object with maximum temperature and the date it is recorded, minimum temperature and
            the date when it is recorded, maximum humidity and the date it is recorded is assigned by respective values
            from that month.
        """

        # Using the lambda function to pass an extra parameter for the max function. That extra parameter is the value
        # at the index of that specific reading.
        max_temp_entry = max(weather_readings, key=lambda x: x.temperature.max)
        max_temp = max_temp_entry.temperature.max
        max_temp_date = max_temp_entry.date

        min_temp_entry = min(weather_readings, key=lambda x: x.temperature.min)
        min_temp = min_temp_entry.temperature.min
        min_temp_date = min_temp_entry.date

        max_humidity_entry = max(weather_readings, key=lambda x: x.humidity.max)
        max_humidity = max_humidity_entry.humidity.max
        max_humidity_date = max_humidity_entry.date

        sum_highest_temp = 0
        sum_lowest_temp = 0
        sum_mean_humidity = 0

        for reading in weather_readings:
            sum_highest_temp += reading.temperature.max
            sum_lowest_temp += reading.temperature.min
            sum_mean_humidity += reading.humidity.mean

        avg_highest_temp = sum_highest_temp // len(weather_readings)
        avg_lowest_temp = sum_lowest_temp // len(weather_readings)
        avg_mean_humidity = sum_mean_humidity // len(weather_readings)

        calculations = ReportStats()
        calculations.set_extremes(max_temp, max_temp_date, min_temp, min_temp_date, max_humidity, max_humidity_date)
        calculations.set_averages(avg_highest_temp, avg_lowest_temp, avg_mean_humidity)

        return calculations
