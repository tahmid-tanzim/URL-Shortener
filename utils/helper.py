import time


def get_hash_char(remainder):
    _DEC = 32
    if 0 <= remainder <= 9:
        _DEC = 48 + remainder
    elif 10 <= remainder <= 35:
        _DEC = 87 + remainder
    elif 36 <= remainder <= 61:
        _DEC = 29 + remainder
    return chr(_DEC)


def get_milli_shortcode():
    millisecond = round(time.time() * 1000)
    value = millisecond
    hash_string = str()
    while value > 0:
        remainder = value % 62
        hash_string = get_hash_char(remainder) + hash_string
        value //= 62
    return millisecond, hash_string
