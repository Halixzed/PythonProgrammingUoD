def count_words(filename):
      """ Write your code here """
  new_list = []
  count = 0
  with open(filename, "r") as f:
    list = f.readlines()
    for x in list:
      new_list.append(x.split())
    for y in new_list:
      for z in y:
        count += 1    
  return (count)
  
def main():
  print(count_words("example.txt")) # should print 15

if __name__ == "__main__":
  main()