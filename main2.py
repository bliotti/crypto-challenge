def xor_b(a, b):
    return bytes([b1 ^ b2 for b1, b2 in zip(a, b)])


def main():
    a = bytes.fromhex('1c0111001f010100061a024b53535009181c')
    b = bytes.fromhex('686974207468652062756c6c277320657965')
    c = xor_b(a, b).hex()
    print(a, b, c)
    return c


# if __name__ == '__main__':
#     main()

assert main() == '746865206b696420646f6e277420706c6179'
