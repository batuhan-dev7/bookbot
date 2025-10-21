#!/usr/bin/python3
from stats import get_total_word_count, character_count, sort_dict

import sys

if len(sys.argv) != 2:
  print("Usage: python3 main.py <path_to_book>")
  sys.exit(1)

def main():
  path_for_frankenstein = sys.argv[1]

  text = get_book_text(path_for_frankenstein)
  word_count = get_total_word_count(text)

  char_count = character_count(text)
  #print(char_count)

  #print(sort_dict(char_count))

  print("============ BOOKBOT ============") 
  print(f"Analyzing book found at {sys.argv[1]}")
  print("----------- Word Count ----------") 
  print(f"Found {word_count} total words")
  print("--------- Character Count -------")

  for dict in sort_dict(char_count):
    if dict["key"].isalpha():
      print(f"{dict['key']}: {dict['num']}")
  
  print("============= END ===============")


def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

main()