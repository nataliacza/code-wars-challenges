from challenges.a_chain_adding_function import add

def test_single_function_call_returns_1():
    result = add(1)
    assert result == 1

def test_single_function_call_returns_5():
    result = add(5)
    assert result == 5

def test_single_function_call_returns_0():
    result = add(0)
    assert result == 0

def test_two_function_call_returns_10():
    result = add(3)(7)
    assert result == 10

def test_five_function_call_returns_26():
    result = add(3)(7)(5)(1)(10)
    assert result == 26
