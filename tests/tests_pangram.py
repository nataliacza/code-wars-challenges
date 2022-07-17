from challenges.pangram import is_pangram

def tests_basic1():
    result = is_pangram("The quick, brown fox jumps over the lazy dog!")
    expected = True
    assert result == expected
