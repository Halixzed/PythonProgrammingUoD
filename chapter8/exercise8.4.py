from collections import Counter

def count_letters(filename):
  new_list = []
  with open(filename, 'r') as f:
    words = f.readlines()
    for x in words:
      for y in x:
        y = y.strip()
        new_list.append(y)
    counts = Counter(new_list)
    keys = list(counts.keys())
    keys.sort()
    sorted_dict = {x: counts[x] for x in keys}
    remove_list = list(sorted_dict)
    for x in remove_list:
      if x == '':
        del sorted_dict['']
      if x == '.':
        del sorted_dict['.']
      if x == ',':
        del sorted_dict[',']
    print(f"The count of the letters for the file {filename} is:\n")
    for x, y in sorted_dict.items():
      print (f"{x}: {y}")
    
if __name__ == "__main__":
  count_letters("words.txt")