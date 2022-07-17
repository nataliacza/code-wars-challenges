'''
https://www.codewars.com/kata/523a86aa4230ebb5420001e1
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true
'abba' & 'bbaa' == true
'abba' & 'abbba' == false
'abba' & 'abca' == false
Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an
array with words. You should return an array of all the anagrams or an empty array if there are none.
'''

from collections import Counter

def anagrams(word, words):
    count_word_letters = dict(Counter(word))
    matching_words = [element for element in words if dict(Counter(element)) == count_word_letters]
    return matching_words

#print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
