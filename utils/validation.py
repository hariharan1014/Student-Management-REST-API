def check_int(value):
    value=value.strip()
    if value is None:
        return False, "value should be entered"
    elif not str(value).isdigit():
        return False, f"{value} should be contains numbers"
    elif int(value) < 0:
        return False, f"{value} should be greater than 0"
    return True, None
def check_str(value):
    value=value.strip()
    if value is None:
        return False, "value should be entered"
    elif not str(value).isalpha():
        return False, f"{value} should be alphabets"
    return True, None
def check_phone(value):
    value=value.strip()
    if value is None:
        return False, "value should be entered"
    value=str(value)
    if not value.isdigit():
        return False, f"{value} should be numbers"
    elif len(value) != 10:
        return False, f"{value} should contain 10 numbers"
    return True, None