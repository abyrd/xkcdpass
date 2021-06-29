#!/usr/bin/python
import random
dict = open ("/usr/share/dict/web2")
words = [line.strip() for line in dict.readlines() if line[-3:] != "'s\n"]
dict = open ("/usr/share/dict/web2a")
words += [line.strip() for line in dict.readlines() if line[-3:] != "'s\n"]
for i in range(20):
    print ' '.join(random.sample(words, 4))

