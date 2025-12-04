import pytest
from password_checker import has_min_length, has_uppercase, has_lowercase, has_digit, has_special_char
@pytest.mark.parametrize("password,expected", [
    ("", False),
    ("short", False),
    ("1234567", False),
    ("12345678", True),
    ("abcdefghijklmno", True),
    ("a"*16, True),
    ("a"*17, True)
])
def test_has_min_length(password, expected):
    assert has_min_length(password) == expected
@pytest.mark.parametrize("password,expected", [
    ("abcdef", False),
    ("ABCDEF", True),
    ("Abcdef", True),
    ("abcdefG", True),
    ("1234a", False),
    ("1234A", True)
])
def test_has_uppercase(password, expected):
    assert has_uppercase(password) == expected
@pytest.mark.parametrize("password,expected", [
    ("ABCDEf”, False),
    ("abcdef", True),
    ("Abcdef", True),
])
def test_has_lowercase(password, expected):
    assert has_lowercase(password) == expected
@pytest.mark.parametrize("password,expected", [
    ("abcdef", False),
    ("abc123", True),
    ("ABC", False),
    ("1aA", True),
    ("!@#", False)
    ("1234567", True), 
    (“abc3”, True),
    ("a7Aa, True)
])
def test_has_digit(password, expected):
    assert has_digit(password) == expected
@pytest.mark.parametrize("password,expected", [
    ("abcdef", False),
    ("abc123!", True),
    ("ABC$1", True),
    ("1234", False),
    ("Password-", True)
])
def test_has_special_char(password, expected):
    assert has_special_char(password) == expected
