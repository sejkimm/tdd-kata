# /tests/test_string_calculator.py

import pytest

from tdd_kata.string_calculator import StringCalculator


@pytest.fixture(scope="module")
def string_calculator():
    string_calculator = StringCalculator()
    yield string_calculator


def test_add_empty_string_expect_0(string_calculator):
    input_string = ""
    result = string_calculator.Add(input_string)

    assert result == 0


def test_add_one_number_string_expect_same(string_calculator):
    input_string = "1"
    result = string_calculator.Add(input_string)

    assert result == 1


def test_add_two_number_string_expect_sum(string_calculator):
    input_string = "1,2"
    result = string_calculator.Add(input_string)

    assert result == 3


def test_add_five_number_string_expect_sum(string_calculator):
    input_string = "1,2,3,4,5"
    result = string_calculator.Add(input_string)

    assert result == 15


def test_add_three_number_string_with_newline_expect_sum(string_calculator):
    input_string = "1\n2,3"
    result = string_calculator.Add(input_string)

    assert result == 6


def test_add_two_number_string_with_semicolon_delimiter_expect_sum(string_calculator):
    input_string = "//;\n1;2"
    result = string_calculator.Add(input_string)

    assert result == 3


def test_add_three_number_string_with_full_comma_delimiter_expect_sum(
    string_calculator,
):
    input_string = "//.\n1.2.3"
    result = string_calculator.Add(input_string)

    assert result == 6
