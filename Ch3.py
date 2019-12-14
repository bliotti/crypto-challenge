# Single-byte XOR cipher
# The hex encoded string:

# 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# ... has been XOR'd against a single character. Find the key, decrypt the message.

# You can do this by hand. But don't: write code to do it for you.

# How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.

hexString = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'


def xor_buffer(a, b):
    return bytes([b1 ^ b for b1 in a])


def areWords(z):
    count = 0
    for a in z:
        # print(a)
        if ((a > 65) and (a < 122)) or (a == 32):
            count += 1
    return count


def decodeByLetter(hs):
    a = bytes.fromhex(hs)
    max = 0
    winner = ""
    winnerChr = ""
    for b in range(122):
        c = xor_buffer(a, b)
        if areWords(c) > max:
            max = areWords(c)
            winner = c
            winnerChr = b
    # print(winner.decode("utf-8"))
    return winner


decodeByLetter(hexString)
