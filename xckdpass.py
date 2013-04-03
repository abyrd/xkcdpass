#!/usr/bin/python
import random
dict = open ("/usr/share/dict/american-english")
words = [line.strip() for line in dict.readlines() if line[-3:] != "'s\n"]
for i in range(20):
    print ' '.join(random.sample(words, 4))

