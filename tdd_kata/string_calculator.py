# /tdd_kata/string_calculator.py


class StringCalculator(object):
    def __init__(self) -> None:
        pass

    def Add(self, numbers: str):
        if numbers.startswith("//"):
            delimiter = numbers[2]
            numbers = numbers[4:]
        else:
            delimiter = ","

        numbers = numbers.replace("\n", delimiter)

        try:
            list_numbers = list(map(int, numbers.split(delimiter)))
            result = sum(list_numbers)
        except ValueError:
            result = 0

        return result
