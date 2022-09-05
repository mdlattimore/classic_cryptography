# Transposition Cipher Encrypt/Decrypt File
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

# TODO Improve using pathlib

import time, os, sys
from transposition_cipher import transposition_encrypt, transposition_decrypt

def main():
    inputFilename = "frankenstein.txt"
    outputFilename = "frankenstein_encrypted.txt"
    myKey = 10
    myMode = 'encrypt'

    # If the input file does not exist, the program terminates early:
    if not os.path.exists(inputFilename):
        print(f"The file {inputFilename} does not exist. Quitting ...")
        sys.exit()
    
    # If the output file already exists, give the user the option to quit
    if os.path.exists(outputFilename):
        print(f"This will overwrite the file {outputFilename}. (C)ontinue or (Q)uit?")
        response = input("> ")
        if not response.lower().startswith("c"):
            sys.exit()

    # Read in the message from the input file
    with open(inputFilename, mode="r") as file:
        content = file.read()

    print(f"{myMode.title()}ing")

    # Measure how long the encryption/decryption takes:
    start = time.perf_counter()
    if myMode == 'encrypt':
        translated = transposition_encrypt(myKey, content)
    elif myMode == 'decrypt':
        translated = transposition_decrypt(myKey, content)
    stop = time.perf_counter()
    print(f"{myMode.title()}ion time: {stop - start} seconds.")

    # Write the translated message to the output file
    with open(outputFilename, mode="w") as file:
        file.write(translated)

    print(f"Done {myMode}ing {inputFilename}, ({len(content)} characters.")
    print(f"{myMode.title()}ed file is {outputFilename}")


if __name__ == '__main__':
    main()