# pylint: disable=missing-module-docstring, invalid-name, too-few-public-methods


class StringCalculator:
    """
    String Calculator
    """

    def __init__(self) -> None:
        pass

    def Add(self, numbers: str):
        """
        Get String of numbers and return sum of them


        :param
            numbers: str - String of numbers

        :return
            result: int - Sum of numbers
        """
        if numbers.startswith("//"):
            delimiter = numbers[2]
            numbers = numbers[4:]
        else:
            delimiter = ","

        numbers = numbers.replace("\n", delimiter)

        try:
            list_numbers = list(map(int, numbers.split(delimiter)))
            negatives = [number for number in list_numbers if number < 0]

            if negatives:
                raise NegativeNumberError(str(negatives))

            result = sum(list_numbers)
        except ValueError:
            result = 0

        return result


class NegativeNumberError(Exception):
    """
    Exception when given string includes negative number
    """

    def __init__(self, msg: str) -> None:
        super().__init__("negatives not allowed - " + msg)
