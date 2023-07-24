# A pangram is a string that contains every letter of
# the alphabet. Given a sentence determine whether it is
# a pangram in the English alphabet. Ignore case.
# Return either pangram or not pangram as appropriate.
#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    alpha = sorted(set(("".join(s.split(" "))).lower()))
    if len(alpha) == 26:
        return "Is a pangram"
    return "Not a pangram"


s = "We promptly judged antique ivory buckles for the prize"
# s = "The quick brown fox jumps over the lazy dog"

print(pangrams(s))
