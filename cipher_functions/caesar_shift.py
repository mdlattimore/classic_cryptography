""" Traditional Caesar Cipher encryption and decryption functions.
Notice that a whitespace is part of the character set """

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890"

def caesar_encrypt(clear_text, key):
    clear_text = clear_text.upper()
    cipher_text = ""
    for char in clear_text:
        if char in SYMBOLS:
            char_idx = SYMBOLS.find(char)
            translated_idx = (char_idx + key) % len(SYMBOLS)  # mod len(SYMBOLS) handles wrap around
            cipher_text += SYMBOLS[translated_idx]
        else:
            cipher_text += char
    return cipher_text


def caesar_decrypt(cipher_text, key):
    cipher_text = cipher_text.upper()
    clear_text = ""
    for char in cipher_text:
        if char in SYMBOLS:
            char_idx = SYMBOLS.find(char)
            translated_idx = (char_idx - key) % len(SYMBOLS) # mod len(SYMBOLS) handles wrap around
            clear_text += SYMBOLS[translated_idx]
        else:
            clear_text += char
    return clear_text


if __name__ == '__main__':
    import pyperclip
    while True:
        print()
        print("(1) encrypt or (2) decrypt?")
        choice = input("> ")
        if choice in ["1", "2"]:
            break
        else:
            continue
    print()
    print("Message to be encrypted/decrypted:")
    text = input("> ")
    print()
    while True:
        try:
            key = int(input("Select a key: "))
            break
        except ValueError:
            print("Enter an integer only")
            continue
    print()
    if choice == "1":
        enc_msg = caesar_encrypt(text, key)
        print(enc_msg)
        pyperclip.copy(enc_msg)
    else:
        dec_msg = caesar_decrypt(text, key)
        print(dec_msg)
        pyperclip.copy(dec_msg)
        

