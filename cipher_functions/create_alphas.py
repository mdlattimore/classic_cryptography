""" Generates dictionary containing 26 alphabets, each shifted one position
from the previous alphabet. """

from collections import deque
import string

letter_set = string.ascii_uppercase

alphabets = dict()
a = deque(letter_set)
for letter in letter_set:
    alphabets[letter] = list(a)
    a.rotate(-1)
   

for key, value in alphabets.items():
    print(f"{key}: {value}")

