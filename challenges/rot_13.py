"""
https://www.codewars.com/kata/530e15517bc88ac656000716/train/python

ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in
the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special
characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet
should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""
import string


def get_excluded_chars() -> list:
    """ Function that returns excluded chars. There is an option to extend or modify. """
    digits_ = list(string.digits)
    punctuation_ = list(string.punctuation)
    white_ = list(string.whitespace)

    return digits_ + punctuation_ + white_


# Setting here dict of chars with indexes - dict, as it's easier to fetch
_CHAR_AS_KEY = {v: i for i, v in enumerate(string.ascii_lowercase)}
_INDEX_AS_KEY = {i: v for i, v in enumerate(string.ascii_lowercase)}

# Setting here list of excluded chars
_EXCLUDED_CHARS = get_excluded_chars()


def encode_letter(char: str) -> str:
    """ Function that takes one letter and returns adequate letter as per rot13 system. """
    get_index = _CHAR_AS_KEY.get(char)

    loop_index = (get_index+13) % len(_CHAR_AS_KEY)
    get_index = loop_index

    result_char = _INDEX_AS_KEY.get(get_index)

    return result_char


def rot13(message):
    """ Main string encoding function. Uses encode_letter function for each letter. Excluded letters
    are copied as they are. Returns encoded string. """
    encoded_result = ""

    for letter in message:
        if letter in _EXCLUDED_CHARS:
            encoded_result += letter
        else:
            is_upper = letter.upper() == letter
            res = encode_letter(letter.lower())
            if is_upper:
                encoded_result += res.upper()
            else:
                encoded_result += res

    return encoded_result

result = rot13('abcdefghijklmnopqrstuvwxyz')
print(result)
