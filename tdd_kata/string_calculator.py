# pylint: disable=missing-module-docstring, invalid-name

import re


class StringCalculator:
    """
    String Calculator
    """

    def __init__(self) -> None:
        pass

    def Add(self, numbers: str) -> int:
        """
        Get String of numbers and return sum of them

        :param
            numbers: str - String of numbers

        :return
            result: int - Sum of numbers
        """

        delimiter = ","

        if numbers.startswith("//"):
            delimiter, number_start = self.get_delimiter(numbers)
            numbers = numbers[number_start:]

        numbers = numbers.replace("\n", delimiter)

        try:
            list_numbers = list(map(int, numbers.split(delimiter)))
        except ValueError:
            result = 0
            return result

        self.check_negative(list_numbers)
        list_numbers = self.ignore_over(list_numbers, threshold=1000)

        result = sum(list_numbers)
        return result

    def get_delimiter(self, numbers: str) -> tuple:
        """
        Get String of numbers and return delimiter of them

        :param
            numbers: str - String of numbers

        :return
            (delimiter, number_start): tuple

            - delimiter: str - Delimiter of numbers(param)
            - number_start: int - First index where actual number string starts
        """

        delimiter = numbers[2]
        number_start = 4

        long_delimiter_pattern = re.compile(r"\/\/\[.+\]")
        matched_delimiter_pattern = re.match(long_delimiter_pattern, numbers)

        if matched_delimiter_pattern:
            delimiter = numbers[3 : matched_delimiter_pattern.end() - 1]
            number_start = matched_delimiter_pattern.end() + 1

        return delimiter, number_start

    def check_negative(self, list_numbers: list) -> None:
        """
        Get String of numbers and raise NegativeNumberError if numbers include negative number

        :param
            list_numbers: list - List of Integer numbers

        :return
            None
        """

        negatives = [number for number in list_numbers if number < 0]

        if negatives:
            raise NegativeNumberError(str(negatives))

    def ignore_over(self, list_numbers: list, threshold: int) -> list:
        """
        Get List of numbers and threshold, return list of numbers under or same threshold value

        :param
            list_numbers: list - List of Integer numbers

        :return
            filtered_list_numbers: list - List of filtered Integer numbers (<= threshold)
        """

        filtered_list_numbers = [
            number for number in list_numbers if number <= threshold
        ]
        return filtered_list_numbers


class NegativeNumberError(Exception):
    """
    Exception when given string includes negative number
    """

    def __init__(self, msg: str) -> None:
        super().__init__("negatives not allowed - " + msg)
