from __future__ import division
import string


cipher = ("ifweallunitewewillcausetheriverstostainthegreatwaterswiththeirblood")

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letterGoodness = (zip(string.ascii_lowercase,
                          [.0817, .0149, .0278, .0425, .1270, .0223, .0202,
                           .0609, .0697, .0015, .0077, .0402, .0241, .0675,
                           .0751, .0193, .0009, .0599, .0633, .0906, .0276,
                           .0098, .0236, .0015, .0197, .0007]))


def rotate(cipher_string, shift):
    plain = ""
    for i in cipher_string:
        plain += (alphabet[(ord(i) - ord('a') + shift) % 26])
    return plain


def frequency_analysis(text):
    letter_count = [0] * 26
    for i in text:
        if i != ' ' and i != '\n':
            letter_count[ord(i) - ord('a')] += 1

    letter_freq = [0] * 26
    for i in range(len(letter_count)):
        letter_freq[i] = (letter_count[i] / len(text))

    return zip(string.ascii_lowercase,letter_freq);

print rotate(cipher, 11)
for i in frequency_analysis(cipher):
    print i[1]
