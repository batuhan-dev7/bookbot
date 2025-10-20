
def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

def main():
  path_for_frankenstein = "books/frankenstein.txt"

  content = get_book_text(path_for_frankenstein)
  print(content)

main()