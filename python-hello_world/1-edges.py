#!/usr/bin/python3
word = "Holberton"
word_first_3, *_, word_last_2 = word
middle_word = "".join(_)
print("First 3 letters: {}".format(word_first_3))
print("Last 2 letters: {}".format(word_last_2))
print("Middle word: {}".format(middle_word))