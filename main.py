from stats import get_book_text, get_total_word_count

def main():
  path_for_frankenstein = "books/frankenstein.txt"

  text = get_book_text(path_for_frankenstein)
  word_count = get_total_word_count(text)
  print(f"Found {word_count} total words")


main()