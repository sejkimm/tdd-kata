# pylint: disable=missing-module-docstring, invalid-name


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
            delimiter = self.get_delimiter(numbers)
            numbers = numbers[4:]

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

    def get_delimiter(self, numbers: str) -> str:
        """
        Get String of numbers and return delimiter of them

        :param
            numbers: str - String of numbers

        :return
            delimiter: str - Delimiter of numbers(param)
        """

        delimiter = numbers[2]
        return delimiter

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
