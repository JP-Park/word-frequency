import re
from collections import Counter

# def word_frequency(file):
with open("sample.txt") as sample:
        text = sample.read().lower()
        # int sample = 0
        # sample = open("sample.txt", 'r')
        # for countWords in sample:
        #     re.search([a-z])
        for line in text.split():
            print(line)
