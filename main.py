#!/usr/share/env python3

#  _   _     _                 _     _     _
# | | | |___(_)_ __   __ _    | |   (_)___| |_
# | | | / __| | '_ \ / _` |   | |   | / __| __|
# | |_| \__ \ | | | | (_| |   | |___| \__ \ |_
#  \___/|___/_|_| |_|\__, |___|_____|_|___/\__|
#                    |___/_____|


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    num_letters.sort()

    print("--- Begin report of books/frankenstein.txt ---")
    print("")
    print(f"{num_words} words found in the document.")
    print("")
    for i in range(len(num_letters)):
        if num_letters[i][0].isalpha():
            print(
                f"The `{num_letters[i][0]}` character was found {num_letters[i][1]} times")

    print("")
    print("--- End report ---")


def get_num_letters(text):
    letter_count = {}
    for i in text.lower():
        if i in letter_count:
            letter_count[i] += 1
        else:
            letter_count[i] = 1
    letter_list = list(letter_count.items())

    return letter_list


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
