from challenges.vowel_count import get_count

def test_vowel1():
    result = get_count("aeiou")
    expected = 5
    assert result == expected

def test_vowel2():
    result = get_count("y")
    expected = 0
    assert result == expected

def test_vowel3():
    result = get_count("bcdfghjklmnpqrstvwxz y")
    expected = 0
    assert result == expected

def test_vowel4():
    result = get_count("")
    expected = 0
    assert result == expected

def test_vowel5():
    result = get_count("abracadabra")
    expected = 5
    assert result == expected
