#!/usr/share/env python3


#  _   _     _                 ____  _      _   _
# | | | |___(_)_ __   __ _    |  _ \(_) ___| |_(_) ___  _ __   __ _ _ __ _   _
# | | | / __| | '_ \ / _` |   | | | | |/ __| __| |/ _ \| '_ \ / _` | '__| | | |
# | |_| \__ \ | | | | (_| |   | |_| | | (__| |_| | (_) | | | | (_| | |  | |_| |
#  \___/|___/_|_| |_|\__, |___|____/|_|\___|\__|_|\___/|_| |_|\__,_|_|   \__, |
#                    |___/_____|                                         |___/


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)

    print("--- Begin report of books/frankenstein.txt ---")
    print("")
    print(f"{num_words} words found in the document.")
    print("")
    for i in num_letters:

        if i.isalpha():

            print(
                f"The `{i}` character was found {num_letters[i]} times")

    print("")
    print("--- End report ---")


def get_num_letters(text):
    letter_count = {}
    for i in text.lower():
        if i in letter_count:
            letter_count[i] += 1
        else:
            letter_count[i] = 1

    return letter_count


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
