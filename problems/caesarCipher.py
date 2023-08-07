# Julius Caesar protected his confidential information by encrypting it using a cipher.
# Caesar's cipher shifts each letter by a number of letters. If the shift takes you past
# the end of the alphabet, just rotate back to the front of the alphabet. In the case of a
# rotation by 3, w, x, y and z would map to z, a, b and c.


def caesarCipher(s, k):
    # ascii values for characters
    temp = []

    # convert char to ascii value
    for char in s:
        temp.append(ord(char))

    # main logic - shifting
    for i in range(len(temp)):
        # uppercase ascii range = 65-90
        if 65 <= temp[i] <= 90:
            # this will shift the characters by k
            temp[i] = (65 + (temp[i] - 65 + k) % 26)

        # lowercase ascii range = 97-122
        elif 90 <= temp[i] <= 122:
            temp[i] = (97 + (temp[i] - 97 + k) % 26)

    return ''.join(map(chr, temp))


s = "abc-Outz"
k = 2
print(caesarCipher(s, k))
