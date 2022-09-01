from collections import Counter
import re

text = input("Please enter text: ")
processed_text = re.sub(r'[^\w\s]', '', text.lower())  # a regex that strips
# punctuation from string
len_text = len(processed_text)

print("*" * 40)
print()
print("Letter Frequency")
letter_list = [letter for letter in processed_text if letter.isalpha()]  #
# even though we've stripped punctuation,
# still test for isalpha() to exclude spaces from analysis

letter_count = Counter(letter_list)
letter_count_sorted = {k: v for k, v in sorted(letter_count.items(), key=lambda
                       item: item[1], reverse=True)}  # sorts dictionary by
# value

for key, value in letter_count_sorted.items():
    print(f"{key}: {value}")
print(f"There are {len_text} letters in this text (not including spaces or "
      f"punctuation marks).")

print("*" * 40)
print()
print("Word Frequency")
word_list = [word for word in processed_text.split()]
len_word_list = len(word_list)

word_count = Counter(word_list)
word_count_sorted = {k: v for k, v in sorted(word_count.items(), key=lambda
                     item: item[1], reverse=True)}

for key, value in word_count_sorted.items():
    print(key, value)
print(f"There are a total of {len_word_list} words in this text.")
print(f"There are {len(word_count)} unique words in this text.")
