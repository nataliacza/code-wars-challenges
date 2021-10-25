'''
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence
"The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is
irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and
punctuation.

pangram = "The quick, brown fox jumps over the lazy dog!"
test.assert_equals(is_pangram(pangram), True)
'''

import string


def is_pangram(sentence):
    correct_result = list(string.ascii_lowercase)
    my_list = sorted(set(item.lower() for item in sentence if item.lower() in correct_result))
    if my_list == correct_result:
        return True
    return False


print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
print(is_pangram("Pack my box with five dozen liquor jugs"))
