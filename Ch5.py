a = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
key = "ICE"
result = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'


def xor_buffer(a, b):
    return bytes([a ^ b])


def decodeByLetter(hs):
    ans = ""
    for b in range(len(a)):
        letter = key[b % len(key)]
        b1 = ord(letter)
        b2 = ord(hs[b])
        res = xor_buffer(b1, b2).hex()
        ans += res
#     print(ans)
    return ans


assert result == decodeByLetter(a)
