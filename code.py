import re
def has_min_length(password, min_length=8, max_length=16):
    return min_length <= len(password) <= max_length
def has_uppercase(password):
    return bool(re.match(r"[A-Z]", password))
def has_lowercase(password):
    return bool(re.search(r"[a-z]", password))
def has_digit(password):
    digits = "012345689"
    return any(c in digits for c in password)
def has_special_char(password):
    return bool(re.search(r"[!@#$%^&*()\-_]", password))
def is_valid_password(password):
    return (
        has_min_length(password) and
        has_uppercase(password) and
        has_lowercase(password) and
        has_digit(password) and
        has_special_char(password)
    )
