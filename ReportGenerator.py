"""
    This module provides a class, `ReportGenerator`, for generating reports based on CLI arguments.

Usage
-----
    from ReportGenerator import ReportGenerator

    # Create an instance of ReportGenerator
    report_generator = ReportGenerator()

    # Generate the report based on the provided arguments
    report_generator.generate_report(*args)
"""

import glob
from FileParser import FileParser
from ComputeResults import ComputeResults
from datetime import datetime


class ReportGenerator:
    """
    A class that will generate reports.

    Methods
    -------
    generate_report
        Calls the appropriate functions according to the CLI arguments.

    yearly_report
        For a given year display the highest and lowest temperature and day, most humid day and humidity.

    monthly_report
        For a given month display the average highest and average lowest temperature, average mean humidity.

    bar_chart_report
        For a given month draw a horizontal bar with the lowest temperature in blue and the highest temperature in red.
    """

    def __init__(self) -> None:
        pass

    def yearly_report(self, files) -> None:
        """
        For a given year display the highest and lowest temperature and day, most humid day and humidity.

        Parameters
        ----------
        files : list
            A list of files with name similar to the one passed by the user.
            Must contain at one value.
        """

        file_parser = FileParser(files[0])
        reading_list = file_parser.parse_file()
        weather_readings = file_parser.populate(reading_list)
        compute = ComputeResults()
        selected_results = compute.assign_results(weather_readings)

        for file in files[1:]:
            file_parser = FileParser(file)
            reading_list = file_parser.parse_file()
            weather_readings = file_parser.populate(reading_list)
            compute = ComputeResults()
            results = compute.assign_results(weather_readings)

            if results.highest_temperature > selected_results.highest_temperature:
                selected_results.highest_temperature = results.highest_temperature
                selected_results.highest_temperature_day = results.highest_temperature_day

            if results.lowest_temperature < selected_results.lowest_temperature:
                selected_results.lowest_temperature = results.lowest_temperature
                selected_results.lowest_temperature_day = results.lowest_temperature_day

            if results.humidity > selected_results.humidity:
                selected_results.humidity = results.humidity
                selected_results.most_humid_day = results.most_humid_day

        highest_temp_date = datetime.strptime(selected_results.highest_temperature_day,
                                              "%Y-%m-%d").strftime("%B %d")
        print('Highest: {}C on {}'.format(selected_results.highest_temperature,
                                          highest_temp_date))

        lowest_temp_date = datetime.strptime(selected_results.lowest_temperature_day,
                                             "%Y-%m-%d").strftime("%B %d")
        print('Lowest: {}C on {}'.format(selected_results.lowest_temperature,
                                         lowest_temp_date))

        most_humid_date = datetime.strptime(selected_results.most_humid_day,
                                            "%Y-%m-%d").strftime("%B %d")
        print('Humidity: {}% on {}'.format(selected_results.humidity,
                                           most_humid_date))

    def monthly_report(self, file) -> None:
        """
        For a given year display the highest and lowest temperature and day, most humid day and humidity.

        Parameters
        ----------
        file : list
            A list that contains the name of the file that matches the given year and month.
            Will always contain one value.
        """

        file_parser = FileParser(file)
        readings_list = file_parser.parse_file()
        weather_readings = file_parser.populate(readings_list)

        compute = ComputeResults()
        results = compute.assign_results(weather_readings)

        print('Highest Average: {}C'.format(results.highest_average_temperature))
        print('Lowest Average: {}C'.format(results.lowest_average_temperature))
        print('Average Mean Humidity: {}%'.format(results.average_of_mean_humidity))

    def bar_chart_report(self, file) -> None:
        """
        For a given month draw a horizontal bar with the lowest temperature in blue and the highest temperature in red.

        Parameters
        ----------
        file : list
            A list that contains the name of the file that matches the given year and month.
            Will always contain one value.
        """

        file_parser = FileParser(file)
        readings_list = file_parser.parse_file()
        weather_readings = file_parser.populate(readings_list)

        for index, reading in enumerate(weather_readings):
            print(str(index + 1) + "\033[34m+\033[0m" * reading.temperature.min, end='')
            print("\033[31m+\033[0m" * reading.temperature.max, '{}C - {}C'.format(reading.temperature.min,
                                                                                   reading.temperature.max))

    # noinspection DuplicatedCode
    def generate_report(self, *args) -> None:
        """
        Calls the appropriate functions according to the given arguments.

        Parameters
        ----------
        *args :
            A variable length argument list.
        """

        months = [
            'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',
        ]
        path_to_files_dir = args[0]
        ranges = []

        for i in range(1, len(args)):
            ranges.append(args[i])

        # Using glob.glob function to get a list of all the filenames having the given month or year as wildcard.
        if ranges[2] is not None:
            pattern = f"{path_to_files_dir}/*{ranges[2]}*"
            files = glob.glob(pattern)
            print('\n----Yearly Report----\n')

            self.yearly_report(files)

        if ranges[0] is not None:

            # Get the last word of the range which represents the month. Use that number to get the month's name.
            if len(ranges[0]) > 6:
                month = months[int(ranges[0][-2:]) - 1]
            else:
                month = months[int(ranges[0][-1]) - 1]

            print('\n----Monthly Report----\n')
            print(month + ' ' + ranges[0][:4])
            pattern = f"{path_to_files_dir}/*{month}*"
            file = glob.glob(pattern)

            self.monthly_report(file[0])

        if ranges[1] is not None:

            if len(ranges[1]) > 6:
                month = months[int(ranges[1][-2:]) - 1]
            else:
                month = months[int(ranges[1][-1]) - 1]

            print('\n----Bar Chart Report----\n')
            print(month + ' ' + ranges[1][:4])
            pattern = f"{path_to_files_dir}/*{month}*"
            file = glob.glob(pattern)

            self.bar_chart_report(file[0])
