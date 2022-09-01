""" A Columnar Transposition Cipher """

import math
import pyperclip

def transposition_encrypt(key, msg):
    # Each string in cphertext represents a column in the grid
    ciphertext = [""] * key

    # Loop through each column in ciphertext
    for column in range(key):
        current_idx = column

        # Keep looping until current_idx goes past message length
        while current_idx < len(msg):
            # Place character as current_idx in msg at the
            # end of the current column in the ciphertext list
            ciphertext[column] += msg[current_idx].upper()

            # Move current_idx over one column by key length to get to next column
            current_idx += key

    # Convert ciphertext list back into string
    return "".join(ciphertext)



def transposition_decrypt(key, msg):
    # The transposition decrypt function will simulate the "columns" and
    # "rows" of the grid that the plaintext is writton on by using a list
    # of strings. First we need to calculate a few values

    # The number of "columns" in our transposition grid:
    num_of_columns = int(math.ceil(len(msg) / float(key)))

    # The number of "rows" in our grid:
    num_of_rows = key

    # The number of blank boxes in the last "column" of the grid:
    num_of_blank_boxes = (num_of_columns * num_of_rows) - len(msg)

    # Each string in plaintext represents a columin in the grid:
    plaintext = [''] * num_of_columns

    # The column and row variables point to where in the grid the next
    # character in the encrypted message will go:
    column = 0
    row = 0

    for symbol in msg:
        plaintext[column] += symbol
        column += 1  # Point to the next column

        # If there are no more columns OR we're at a blank box, go back
        # to the first column and next row
        if (column == num_of_columns) or (column == num_of_columns -1 and
            row >= num_of_rows - num_of_blank_boxes):
            column = 0
            row += 1

    return "".join(plaintext)


if __name__ == '__main__':
    import pyperclip
    enc_msg = transposition_encrypt(5, "The only thing we have to fear is fear itself")
    print(enc_msg + "|")
    dec_msg = transposition_decrypt(5, enc_msg)
    print(dec_msg + "|")