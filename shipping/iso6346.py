"""
ISO 6346 shipping container codes.
"""


def create(owner_code, serial, category='U'):
    """Create an ISO 6346 shipping container code.

    Args:
        owner_code (str): Three character alphabetic container code.
        serial (str): Six digit numeric serial number.
        category (str): Equipment category identifier.

    Returns:
        An ISO 6346 container code including a check digit.

    Raises:
        ValueError: If incorrect values are provided.
    """
    if not (len(owner_code) == 3 and owner_code.isalpha()):
        raise ValueError("Invalid ISO 6346 owner code '{}'".format(owner_code))

    if category not in ('U', 'J', 'Z', 'R'):
        raise ValueError("Invalid ISO 6346 category identifier '{}'".format(category))

    if not (len(serial) == 6 and serial.isdigit()):
        raise ValueError("Invalid ISO 6346 serial number")

    raw_code = owner_code + category + serial
    full_code = raw_code + str(check_digit(raw_code))
    return full_code


def check_digit(raw_code):
    """Compute the check digit for an ISO 6346 code without that digit

    Args:
        raw_code (str): An ISO 6346 code lacking a check digit.

    Returns:
        An integer check digit between 0 and 9 inclusive.
    """
    s = sum(code(char) * 2**index for index, char in enumerate(raw_code))
    return s % 11 % 10


def code(char):
    """Determine the ISO 6346 numeric equivalent of a character.

    Args:
        char (str): A single character string.

    Return:
        An integer code equivalent to the supplied character.
    """
    return int(char) if char.isdigit() else letter_code(char)


def letter_code(letter):
    """Determine the ISO 6346 numeric code for a letter.

    Args:
        letter (str): A single letter.

    Returns:
        An integer character code equivalent to the supplied letter.
    """
    value = ord(letter.lower()) - ord('a') + 10
    return value + value // 11
