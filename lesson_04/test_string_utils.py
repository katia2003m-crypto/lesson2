import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# 1. Тесты для функции capitalize (2 теста)


@pytest.mark.positive
@pytest.mark.parametrize("string, expected", [
    ("skypro", "Skypro"),
    ("тест", "Тест")
])
def test_capitalize_positive(string, expected):
    assert string_utils.capitalize(string) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, expected", [
    ("", ""),
    (" ", " ")
])
def test_capitalize_negative(string, expected):
    assert string_utils.capitalize(string) == expected

# 2. Тесты для функции trim (2 теста)


@pytest.mark.positive
@pytest.mark.parametrize("string, expected", [
    (" skypro", "skypro"),
    ("   skypro", "skypro")
])
def test_trim_positive(string, expected):
    assert string_utils.trim(string) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, expected", [
    ("", ""),
    (" ", "")
])
def test_trim_negative(string, expected):
    assert string_utils.trim(string) == expected

# 3. Тесты для функции contains (2 теста)


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False)
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) is expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("", "S", False),
    (" ", " ", True)
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) is expected

# 4. Тесты для функции delete_symbol (2 теста)


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky")
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("", "a", ""),
    ("SkyPro", "Z", "SkyPro")
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected
