def get_total_word_count(text):
  return len(text.split())


#counts each character on top of letters !
def character_count(text): 
  char_counts = {}
  for char in text:
    lower_char = char.lower()
    if lower_char not in char_counts:
      char_counts[lower_char] = 1
    else:
      char_counts[lower_char] += 1
  return char_counts


def sortCriteria(d):
  return d["num"]


def sort_dict(word_count_dict):
  list_of_dicts = []
  for key in word_count_dict:
    dct = {}
    dct["key"] = key
    dct["num"] = word_count_dict[key]
    list_of_dicts.append(dct)
  list_of_dicts.sort(key=sortCriteria, reverse=True)
  return list_of_dicts

