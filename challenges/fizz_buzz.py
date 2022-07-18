class InvalidValueException(Exception):
    pass

def play_fizz_buzz(value: int) -> str:

    fbzz = "FizzBuzz"
    fzz = "Fizz"
    bzz = "Buzz"

    if not is_input_valid(value):
        raise InvalidValueException("Please provide integer!")

    if value % 15 == 0:
        return fbzz
    elif value % 5 == 0:
        return fzz
    elif value % 3 == 0:
        return bzz
    else:
        return "Not a match!"

def is_input_valid(value: int) -> bool:
    if isinstance(value, int):
        return True
    return False
