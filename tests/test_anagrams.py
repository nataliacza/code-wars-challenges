from challenges.where_my_anagrams_at import anagrams

def test_anagrams1():
    result = anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])
    expected_result = ['aabb', 'bbaa']
    assert result == expected_result

def test_anagrams2():
    result = anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])
    expected_result = ['carer', 'racer']
    assert result == expected_result
