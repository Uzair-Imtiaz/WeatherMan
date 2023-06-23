"""
    This module provides a class, `FileParser`, for parsing files and populating the readings data structure with the
    correct data types.

Usage
-----
    from FileParser import FileParser

    # Create an instance of FileParser
    file_parser = FileParser(filename)

    # Parse the file and retrieve the list of readings
    readings_list = file_parser.parse_file()

    # Populate the weatherReadings objects with the readings data
    weather_readings = file_parser.populate(readings_list)
"""

from WeatherReadings import WeatherReadings
import csv


class FileParser:
    """
    A class that parses the files and populates the readings data structure with correct data types.

    Attributes
    ----------
    filename : str
        Stores the name of the file that is to be parsed.

    Methods
    -------
    parse_file
        Parse the file and store the data in a list.

    populate
        Create a list of weatherReadings type with data from the file previously parsed.
    """

    def __init__(self, filename: str) -> None:
        """
        Constructor

        Parameters
        ----------
        filename : str
            Contains the name of the file that will be parsed.
        """

        self.filename = filename

    def parse_file(self) -> list:
        """
        Parse the file and get the list of readings of each day.

        Returns
        -------
        reading_list : list
            List of the lines read from the file.
        """

        reading_list = []
        with open(self.filename, 'r', encoding="utf-8") as records_file:
            reader = csv.reader(records_file)
            next(reader)

            for row in reader:
                reading_list.append(row)

            return reading_list

    def populate(self, reading_list) -> list:
        """
        Creates objects of weatherReadings type for each day and append them to a list.

        Parameters
        ----------
        reading_list : list
            The list of the data read from the file that contains readings for each day of the month.

        Returns
        -------
        weather_readings : list
            The list of weatherReadings type object populated with readings data from the file.
        """

        weather_readings = []
        for reading in reading_list:
            weather_reading = WeatherReadings(reading)
            weather_readings.append(weather_reading)
        return weather_readings
