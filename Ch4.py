# https://cryptopals.com/sets/1/challenges/4
# Detect single-character XOR
# One of the 60-character strings in this file has been encrypted by single-character XOR.

# Find it.

# (Your code from #3 should help.)
from Ch3 import decodeByLetter, areWords

f = open("Ch4.txt", "r")
max = 0
for x in f:
    c = areWords(decodeByLetter(x))
    if c >= max:
        max = c
        winner = decodeByLetter(x)
print(winner.decode("utf-8"))
