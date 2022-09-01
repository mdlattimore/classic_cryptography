from caesar_shift import caesar_decrypt, caesar_encrypt
from unicode_shift import unicode_decrypt, unicode_encrypt
from transposition_cipher import transposition_decrypt, transposition_encrypt
from belaso_cipher import belaso_encrypt, belaso_decrypt
import os
import pyperclip

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

schemes = ["Caesar Shift", "Unicode Shift", "Transposition Cipher", "Belaso Cipher"]

clear()
print()
print(" Encryption/Decryption Tool ".center(60, "*"))
print()
print("Select Protocol")
for idx, value in enumerate(schemes):
    print(f"{idx + 1}. {value}")
protocol = int(input("> "))
print()
print("(1) Encrypt or (2) Decrypt")
action = int(input("> "))
print()
print("Message to encrypt/decrypt")
msg = str(input("> "))
print()
if protocol == 1:
    key = int(input("Enter offset: "))
    if action == 1:
        enc_msg = caesar_encrypt(msg, key)
        pyperclip.copy(enc_msg)
        print(enc_msg)
    else:
        dec_msg = caesar_decrypt(msg, key)
        pyperclip.copy(dec_msg)
        print(dec_msg)
elif protocol == 2:
    key = int(input("Enter offset: "))
    if action == 1:
        enc_msg = unicode_encrypt(msg, key)
        pyperclip.copy(enc_msg)
        print(enc_msg)
    else:
        dec_msg = unicode_decrypt(msg, key)
        pyperclip.copy(dec_msg)
        print(dec_msg)
elif protocol == 3:
    key = int(input("Enter key: "))
    if action == 1:
        enc_msg = transposition_encrypt(key, msg)
        pyperclip.copy(enc_msg)
        print(enc_msg)
    else:
        dec_msg = transposition_decrypt(key, msg)
        pyperclip.copy(dec_msg)
        print(dec_msg)
elif protocol == 4:
    key = input("Enter keyword: ")
    if action ==  1:
        enc_msg = belaso_encrypt(msg.upper(), key.upper())  # Belaso function expects .upper() arguments.
        pyperclip.copy(enc_msg)
        print(enc_msg)
    else:
        enc_msg = belaso_decrypt(msg.upper(), key.upper())  # Belaso function expects .upper() arguments.
        pyperclip.copy(enc_msg)
        print(enc_msg)