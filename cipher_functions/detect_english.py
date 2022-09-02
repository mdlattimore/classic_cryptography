# detect_english.py
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

# To use ...
# import detect_english
# detect_english.is_english(string)

UPPERLETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + " \t\n"

def load_dictionary():
    # I've read the explanation and I still don't know why he chose
    # to use a dictionary rather than a list.
    english_words = {}
    with open("dictionary.txt", mode="r") as file:
        dictionary_file = file.read()
    for word in dictionary_file.split("\n"):
        english_words[word] = None
    return english_words

ENGLISH_WORDS = load_dictionary()

def get_english_count(message):
    message = message.upper()
    message = remove_non_letters(message) # called function returns a stgin
    possible_words = message.split()  # creates list from string

    if possible_words == []:
        return 0.0 # No words, so return 0

    matches = 0  # initialize counter
    for word in possible_words:
        if word in ENGLISH_WORDS:
            matches += 1
    return float(matches) / len(possible_words)

def remove_non_letters(message):
    letters_only = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            letters_only.append(symbol)
    return "".join(letters_only)


def is_english(message, word_percentage=20, letter_percentage=85):
    # By default, 20% of the words must exist in the dictionary file
    # 85% of all characters in the message must be letters or spaces
    # (not punctuation or numbers)
    words_match = get_english_count(message) * 100 >= word_percentage
    num_letters = len(remove_non_letters(message))
    message_letters_percentage = float(num_letters) / len(message) * 100
    letters_match = message_letters_percentage >= letter_percentage
    return words_match and letters_match