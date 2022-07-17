from challenges.opposite_number import opposite

def test_1():
    result = opposite(1)
    expected = -1
    assert result == expected

def test_2():
    result = opposite(25.6)
    expected = -25.6
    assert result == expected

def test_3():
    result = opposite(0)
    expected = 0
    assert result == expected

def test_4():
    result = opposite(1425.2222)
    expected = -1425.2222
    assert result == expected

def test_5():
    result = opposite(-3.1458)
    expected = 3.1458
    assert result == expected

def test_6():
    result = opposite(95858588225)
    expected = -95858588225
    assert result == expected
