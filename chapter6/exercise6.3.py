def main():
  list = []
  i = 0
  while i<10:
    num = input("Please enter the next number: ")
    if num == "q":
      break
    list.append(num)
    i = i + 1
  rev = list[::-1]
  if (len(rev) == 0):
    print("No numbers entered.")
  else:
    print("The reverse of the numbers entered is:")
    for x in rev:
      print(x)
    
    
  
  

# This is the entry point of the program
if __name__ == "__main__":
  main() # call the main function