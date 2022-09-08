# Transposition Citpher Hacker
# https://www.nostarch.com/crackingcodes/ (BSD Licensed) 

import pyperclip
from transposition_cipher import transposition_decrypt
from detect_english import is_english

def main():
    my_message = """ae a asadde a asMrsetot n osetot
"""

    hacked_message = hack_transposition(my_message)

    if hacked_message == None:
        print("Failed to hack encryption")
    else:
        print("Copying hacked message to clipboard:")
        print(hacked_message)
        pyperclip.copy(hacked_message)


def hack_transposition(message):
    print("Hacking ...")

    print("(Press Ctrl-C (on Windows) or Ctrl-D (on macOS or Linux) to quit at any time.")

    # Brute force by looping through every possible key:
    for key in range(1, len(message)):
        print(f"Trying key #{key}")

        decrypted_text = transposition_decrypt(key, message)

        if is_english(decrypted_text):
            # Ask user if this is the correct decryption
            print()
            print("Possible encryption hack:")
            print(f"Key {key}: {decrypted_text[:100]}")
            print()
            print("Enter D if done, anything else to continue hacking: ")
            response = input("> ")

            if response.strip().upper().startswith("D"):
                return decrypted_text

    return None


if __name__ == '__main__':
    main()