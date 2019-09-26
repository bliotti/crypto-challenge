

def xor_b(a, b):
    return bytes([b1 ^ b for b1 in a])


def main():
    a = bytes.fromhex(
        '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
    for b in range(256):
        c = xor_b(a, b)
        print(c)
    return c


if __name__ == '__main__':
    main()
