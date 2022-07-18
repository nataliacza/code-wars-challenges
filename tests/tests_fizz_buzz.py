from challenges.fizz_buzz import play_fizz_buzz, InvalidValueException
import unittest

fbzz = "FizzBuzz"
fzz = "Fizz"
bzz = "Buzz"

def tests_fb_when15Given_shouldReturnFizzBuzz():
    result = play_fizz_buzz(15)
    expected_result = fbzz
    assert result == expected_result

def tests_fb_when5Given_shouldReturnFizzBuzz():
    result = play_fizz_buzz(5)
    expected_result = fzz
    assert result == expected_result

def tests_fb_when3Given_shouldReturnFizzBuzz():
    result = play_fizz_buzz(3)
    expected_result = bzz
    assert result == expected_result

def tests_fb_when1Given_shouldReturnMessage():
    result = play_fizz_buzz(1)
    expected_result = "Not a match!"
    assert result == expected_result


class ExceptionTestCase(unittest.TestCase):
    def tests_fb_whenStringGiven_shouldRaiseException(self):
        self.assertRaises(InvalidValueException, play_fizz_buzz, "abc")
