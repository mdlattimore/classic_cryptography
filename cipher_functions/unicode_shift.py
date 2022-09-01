""" Simple encrypt/decrypt functions using Unicode code offset as the key """


def unicode_encrypt(clear_text, key):
    sym_list = [char for char in clear_text]
    utf_coded = [ord(char) for char in sym_list]
    pre_encrypt = [char + key for char in utf_coded]
    encrypt_list = [chr(char) for char in pre_encrypt]
    encrypt_msg = "".join(encrypt_list)
    return encrypt_msg

def unicode_decrypt(cipher_text, key):
    sym_list = [char for char in cipher_text]
    utf_coded = [ord(char) for char in sym_list]
    pre_decrypt = [char - key for char in utf_coded]
    decrypt_list = [chr(char) for char in pre_decrypt]
    decrypt_msg = "".join(decrypt_list)
    return decrypt_msg


if __name__ == '__main__':
    import pyperclip
    print()
    print("Do you wish to (1) encrypt or (2) decrypt a message? ")
    while True:
        choice = input("> ")
        if choice not in ["1", "2"]:
            print("Please select 1 (encrypt) or 2 (decrypt)")
            continue
        else:
            break
    if choice == "1":
        print("Type message to be encrypted")
        clear_text = input("> ")
        print()
        key = int(input("Please select a key: "))
        print()
        print("Encrypted message:")
        encrypted_msg = encrypt(clear_text, key)
        print(encrypted_msg)
        print()
        pyperclip.copy(encrypted_msg)

    else:
        print("Type message to be decrypted")
        cipher_text = input("> ")
        print()
        key = int(input("Please input the key: "))
        print()
        print("Decrypted message:")
        decrypted_msg = decrypt(cipher_text, key)
        print(decrypted_msg)
        print()
        pyperclip.copy(decrypted_msg)