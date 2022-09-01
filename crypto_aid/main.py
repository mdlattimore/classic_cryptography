from letter_counter import letter_count
from contact_map import make_map
from pprint import pprint
import json

print("Enter cryptogram:")
cipher_text = input("> ")
print()
for k, v in letter_count(cipher_text).items():
    print(f"{k}: {v}")
print()
char_map = make_map(cipher_text)
for k, v in char_map.items():
    print("".join(v))

with open("cryptanalysis.txt", mode='w') as file:
    file.write(str(letter_count(cipher_text)))
    file.write(str(make_map(cipher_text)))
