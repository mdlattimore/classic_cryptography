# belaso_cipher.py
# Simple Belaso Cipher
""" This has often been called the Vigenere Cipher after Blaise Vigenere. 
This was invented by Giovan Battista Belaso, not Vigenere, who invented a 
different (but similar) polyalphabetic cipher. """

from collections import deque
import string
import pyperclip


# Use collections.deque rotate() method to create dictionary of alphabets with first letter as key and shifted alphabet as value
letter_list = string.ascii_uppercase

# *****
# This section isn't currently being used and is unnecessary as the program currently stands
# I'm going to keep it here in case I want to use multiple alphabets in the encryption.
# This creates a dictionary of every alphabet shift.
alphabets = dict()
# create deque object
a = deque(letter_list)
for letter in letter_list:
    alphabets[letter] = list(a)  # convert deque object into list and add entry to dictionary
    a.rotate(-1)
# *****    


def belaso_encrypt(msg: str, key: str) -> str:
    enc_msg = ""
    print()
    key_list = [char for char in key]
    key_idx = [letter_list.find(key) for key in key_list]
    key_deque = deque(key_idx)
    for letter in msg:
        if letter == " ":
            enc_msg += letter
        else:
            msg_idx = letter_list.find(letter)
            trans_key = key_deque[0]
            enc_idx = (msg_idx + trans_key) % len(letter_list)
            enc_msg += letter_list[enc_idx]
            key_deque.rotate(-1)
    return enc_msg


def belaso_decrypt(msg: str, key: str) -> str:
    enc_msg = ""
    print()
    key_list = [char for char in key]
    key_idx = [letter_list.find(key) for key in key_list]
    key_deque = deque(key_idx)
    for letter in msg:
        if letter == " ":
            enc_msg += letter
        else:
            msg_idx = letter_list.find(letter)
            trans_key = key_deque[0]
            enc_idx = (msg_idx - trans_key) % len(letter_list)
            enc_msg += letter_list[enc_idx]
            key_deque.rotate(-1)
    return enc_msg



if __name__ == '__main__':
    print()
    print("Message to be encrypted/decrypted")
    msg = input("> ").upper()
    print("Enter keyword")
    key = input("> ").upper()
    choice = int(input("(1) encrypt or (2) decrypt: "))
    if choice == 1:
        msg = belaso_encrypt(msg, key)
        print(msg)
        pyperclip.copy(msg)
    else:
        msg = belaso_decrypt(msg, key)
        print(msg)
        pyperclip.copy(msg)

