from Ch3 import decodeByLetter
from Ch3 import areWords


f = open("demofile.txt", "r")
maxy = 0
for x in f:
    c = areWords(decodeByLetter(x))
    if c >= maxy:
        maxy = c
        winner = decodeByLetter(x)
print(winner)
