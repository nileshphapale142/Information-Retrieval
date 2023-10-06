import random
import string

with open('file.txt', 'w') as f:
    with open('raj.txt', 'r') as word_file:
        words = word_file.readlines()
        for i in range(100):
            f.write(random.choice(words))
        for i in range(2 * 1024 * 1024 // 11 - 1000):
            f.write(random.choice(words))