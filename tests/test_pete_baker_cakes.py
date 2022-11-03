from challenges.pete_baker_cake import cakes


def tests_1():
    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    result = cakes(recipe, available)
    expected_result = 2
    assert result == expected_result

def tests_2():
    recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
    available = {"sugar": 500, "flour": 2000, "milk": 2000}
    result = cakes(recipe, available)
    expected_result = 0
    assert result == expected_result
