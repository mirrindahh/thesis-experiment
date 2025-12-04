import pytest

from code import has_min_length, has_uppercase, has_lowercase, has_digit, has_special_char

'''их сначала починить надо, тут не работает ничего'''
@pytest.mark.parametrize("password,expected", [
    ("", False),
    ("short", False),
    ("1234567", False),
    ("12345678", True),
    ("abcdefghijklmno", True),
    ("a"*16, True),
    ("a"*17, True)
])

# а емае тут сверху для него параметры, не проходит последний тк длина 17, а макс 16
def test_has_min_length(password, expected):
    assert has_min_length(password) == expected


# не проходит abcdef и 1234A почему второй не проходит хз, там вроде нормальный regex на заглавные
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


# ABCDEf должен проходить тк есть маленькая f
# а мы их фиксим вообще или ок.
@pytest.mark.parametrize("password,expected", [
    ("ABCDEf", False),
    ("abcdef", True),
    ("Abcdef", True),
])
def test_has_lowercase(password, expected):
    assert has_lowercase(password) == expected


# a7Aa - нет спецсимволов, должно быть false
@pytest.mark.parametrize("password,expected", [
    ("abcdef", False),
    ("abc123", True),
    ("ABC", False),
    ("1aA", True),
    ("!@#", False),
    ("1234567", True), 
    ("abc3", True),
    ("a7Aa", True)
])
def test_has_digit(password, expected):
    assert has_digit(password) == expected

# тут все ок
@pytest.mark.parametrize("password,expected", [
    ("abcdef", False),
    ("abc123!", True),
    ("ABC$1", True),
    ("1234", False),
    ("Password-", True)
])
def test_has_special_char(password, expected):
    assert has_special_char(password) == expected

# дальше чего
'''
Блок 3. Классификация и обсуждение дефектов – 10–15 минут
A и B обсуждают:
тип ошибки;
приоритет;
дальнейшие действия.

проблемы в тестах везде, кроме test_has_uppercase, там что-то с самой функцией
посмотрим её в первую очередь, дальше поправить тесты, заменить expected = !expected где они не проходят
дальше льем этот код в прод, рубим бабло, туда-сюда миллион. считай папа миллионер
'''