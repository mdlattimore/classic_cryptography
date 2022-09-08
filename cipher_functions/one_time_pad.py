"""A one-time pad encryption and decryption tool. The encryption is done by adding the LETTERS[index] position of each character of the cleartext to the LETTERS[index] position of the corresponding character in the key and then returning the value of the new LETTERS[index] as the enciphered character. Includes a function to create the one-time pad that is the same length as the cleartext"""
# 37 character set including digits and space.

import secrets

# Character Set
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890"

def one_time_encrypt(text: str) -> str:
    ciphertext = ""
    clr_index = []
    for letter in text:
        clr_index.append(LETTERS.find(letter))
    for n in range(len(text)):
        cipher_number = (key_index[n] + clr_index[n]) % len(LETTERS)  # to handle wrap around. Mod must equal the length of LETTERS.
        ciphertext += LETTERS[cipher_number]
    return ciphertext

def one_time_decrypt(text: str) -> str:
    clr_text = ""
    code_idx = []
    for letter in text:
        code_idx.append(LETTERS.find(letter))
    for n in range(len(text)):
        clr_number = (code_idx[n] - key_index[n]) % len(LETTERS)
        clr_text += LETTERS[clr_number]
    return clr_text

def create_pad(n: int) -> str:
    """Create a one-time pad using the random module"""
    pad = ""
    for n in range(n):
        pad += secrets.choice(LETTERS)
    return pad

if __name__ == '__main__':

    msg = input("Enter message: ").upper()
    cleartext = "".join([letter for letter in msg if letter in LETTERS])  # Eliminates characters not in LETTERS

    # Create the one-time pad
    key = create_pad(len(cleartext))

    # Create ordered list of index positions of key characters in the LETTERS variable
    key_index = []
    for letter in key:
        key_index.append(LETTERS.find(letter))


    print(f"Cleartext: {cleartext}")
    print(f"Key: {key}")
    encrypted_msg = one_time_encrypt(cleartext)
    print(f"Encrypted text: {encrypted_msg}")

    # Checks the encryption/decryption accuracy 
    print(one_time_decrypt(encrypted_msg))


# Chart of indexes for quickly checking accuracy of functions
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z _ 1 2 3 4 5 6 7 8 9 0
# 0 1 2 3 4 5 6 7 8 9 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 
#                     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6