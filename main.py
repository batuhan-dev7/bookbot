def main():
  path_for_frankenstein = "books/frankenstein.txt"

  text = get_book_text(path_for_frankenstein)
  word_count = get_total_word_count(text)
  print(f"Found {word_count} total words")


def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()
  

def get_total_word_count(text):
  return len(text.split())


main()