def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()
  

def get_total_word_count(text):
  return len(text.split())