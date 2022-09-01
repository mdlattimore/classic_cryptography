""" Creates a contact map for all letters in text, showing letters to the 
left and right of each character"""

from collections import deque
from process_text import process_text_characters


def make_map(text: str) -> dict:
    # Solely to extract characaters to create a set
    processed_text = process_text_characters(text)
    character_set = set(processed_text)
    text = text.upper()
    # create dictionary from character set. The key is the character, the value is
    # a deque object (list) with the capital key as initial value. 
    dict_map = {}
    for char in character_set:
        dict_map[char.upper()] = deque([" ", char.upper(), " "])
    
    # iterate through characters at word level, mapping letters to the right and left
    for word in text.split():
        for idx, char in enumerate(word):
            if idx > 0:
                dict_map[char].appendleft(word[idx-1].lower())
            if idx < len(word) - 1:
                dict_map[char].append(word[idx+1].lower())
    return dict_map 


if __name__ == '__main__':
    text = "Now is the time for all good men to come to the aid of their country"
    result = make_map(text)

    for kev, value in result.items():
        print(f"{' '.join(list(value))}")
