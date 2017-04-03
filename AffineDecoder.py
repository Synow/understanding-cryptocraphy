import string
# Affine cipher decoder
# Author - Syknow
alphabet = dict(zip( string.ascii_lowercase, range(26)))
cipher = "falszztysyjzyjkywjrztyjztyynaryjkyswarztyegyyj"
cipherNum = map(lambda x: alphabet[x], cipher)
plainNum = []
a1 = 7; b = 22
for i in range(1,26):
    if i * a1 % 26 == 1:
        a2 = i
print 'a2:', i

for i in cipherNum:
    plainNum.append((a2 * (i-b)) % 26)

print(cipherNum)
print(plainNum)
print("Decrypt")

plain = map(lambda x: chr(97 + x), plainNum)
print("".join(plain))
