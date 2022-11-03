from challenges.simple_pig_latin import pig_it

def test_pig1():
    result = pig_it("Pig latin is cool")
    expected = "igPay atinlay siay oolcay"
    assert result == expected

def test_pig2():
    result = pig_it("This is my string")
    expected = "hisTay siay ymay tringsay"
    assert result == expected
