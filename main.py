from stats import get_total_word_count, character_count, sort_dict

def main():
  path_for_frankenstein = "books/frankenstein.txt"

  text = get_book_text(path_for_frankenstein)
  word_count = get_total_word_count(text)

  char_count = character_count(text)
  #print(char_count)

  #print(sort_dict(char_count))

  print("============ BOOKBOT ============") 
  print("Analyzing book found at books/frankenstein.txt...")
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