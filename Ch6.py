a = 'this is a test'
b = 'wokka wokka!!!'


def strToBytes(str):
    return bytes(str, "utf-8")


bytes_1 = strToBytes(a)
bytes_2 = strToBytes(b)

xor_bytes = [b1 ^ b2 for b1, b2 in zip(bytes_1, bytes_2)]

count = 0
for bit in xor_bytes:
    for b in bin(bit):
        if (b == '1'):
            count += 1

print(count)
