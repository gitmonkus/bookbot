#!/usr/bin/env python3
 
def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_char(text):
    char_dict = {}
    for t in text:
        tl = t.lower()
        if tl in char_dict:
            char_dict[tl] += 1
        else:
            char_dict[tl] = 1
    return char_dict 

def get_num_sort(items):
    sort_items = dict(sorted(items.items(), key=lambda item: item[1], reverse=True))
    return sort_items


    




    