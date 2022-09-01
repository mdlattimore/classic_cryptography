from collections import Counter
from process_text import process_text_characters

def letter_count(text: str) -> dict:
    letter_list = process_text_characters(text)
    letter_count = Counter(letter_list)
    letter_count_sorted = {k: v for k, v in sorted(letter_count.items(), key=lambda
        item: item[1], reverse=True)}  # sorts dictionary by value
    return letter_count_sorted

if __name__ == '__main__':
    # text = """The unanimous Declaration of the thirteen united States of America, When in the Course of human events, it becomes necessary for one people to dissolve the political bands which have connected them with another, and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and of Nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation."""
    # text = "AMYMF ZE VE MCTMDD ROV WMV JEIMFSVLEA RM QEOF ZOLIM"
    text = input("Enter text: ")
    parsed_text = letter_count(text)
    for k, v in parsed_text.items():
        print(f"{k}: {v}")
    