import pytest

from challenges.rot_13 import rot13


@pytest.mark.parametrize("message, expected_result", [
    ('test', 'grfg'),
    ('Test', 'Grfg'),
    ('aA bB zZ 1234 *!?%', 'nN oO mM 1234 *!?%'),
    ('abcdefghijklmnopqrstuvwxyz', 'nopqrstuvwxyzabcdefghijklm')
])
def test_rot13_fixed_strings(message, expected_result):
    result = rot13(message)
    assert result == expected_result
