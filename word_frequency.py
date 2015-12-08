import re
from collections import Counter

# def word_frequency(file):
with open("sample.txt") as sample:
        words = re.findall('[a-z]+', sample.read().lower())
        word_count = Counter(words).most_common(20)
        print(word_count)


# text = sample.read().lower()
        # for line in text.split():
        #     print(line)