import time


def current_milli_time():
    return round(time.time() * 1000)


def get_hash_char(remainder):
    _DEC = 32
    if 0 <= remainder <= 9:
        _DEC = 48 + remainder
    elif 10 <= remainder <= 35:
        _DEC = 87 + remainder
    elif 36 <= remainder <= 61:
        _DEC = 29 + remainder
    return chr(_DEC)


def convert_milli_hash(value):
    hash_string = str()
    while value > 0:
        remainder = value % 62
        hash_string = get_hash_char(remainder) + hash_string
        value //= 62
    return hash_string


if __name__ == "__main__":
    print(convert_milli_hash(current_milli_time()))
