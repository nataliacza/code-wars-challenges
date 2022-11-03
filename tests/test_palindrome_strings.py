import pytest

from challenges.palindrome_strings import is_palindrome

@pytest.mark.parametrize("string, expected_result", [
    ("anna", True),
    ("walter", False),
    (12321, True),
    (123456, False)
])
def test_rot13_fixed_strings(string, expected_result):
    result = is_palindrome(string)
    assert result == expected_result
