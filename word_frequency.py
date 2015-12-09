import re
from collections import Counter

with open("sample.txt") as sample:
        words = re.findall('[a-z]+', sample.read().lower())
        word_count = Counter(words).most_common(20)
        for key, value in word_count:
            print(key, value)
