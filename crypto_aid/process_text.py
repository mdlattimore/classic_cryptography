# Scrubs punctuation and white space from text to get accurate count and 
# returns a list of individual letters

import re


def process_text_characters(text: str) -> list:
    processed_text = re.sub(r'[^\w\s]', '', text.lower())  # a regex that strips
    # punctuation from string
    letter_list = [letter for letter in processed_text if letter.isalpha()]  #
    # even though we've stripped punctuation,
    # still test for isalpha() to exclude spaces
    return letter_list

if __name__ == '__main__':
    text = """The unanimous Declaration of the thirteen united States of America, When in the Course of human events, it becomes necessary for one people to dissolve the political bands which have connected them with another, and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and of Nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation."""
    print(process_text_characters(text))