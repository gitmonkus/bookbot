#!/usr/bin/env python3

from stats import get_num_words
from stats import get_num_char
from stats import get_num_sort

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char = get_num_char(text)
    num_sort = get_num_sort(num_char)
    print_report(book_path, num_words, num_sort)
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

   
def print_report(book_path, num_words, num_sort):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for num in num_sort:
        if num.isalpha():
            print(f"{num}: {num_sort[num]}")
    
    print("============= END ===============")



    
main()