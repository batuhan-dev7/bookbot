from stats import get_total_word_count, character_count

def main():
  path_for_frankenstein = "books/frankenstein.txt"

  text = get_book_text(path_for_frankenstein)
  word_count = get_total_word_count(text)
  print(f"Found {word_count} total words")

  char_count = character_count(text)
  print(char_count)


def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

main()