'''Exercise 5.3'''

def num_digits(x = 0):
     # remove the following line and write the function here
  try:
    x = int(input("Please enter a positive whole number:\n"))
    counter = 0
    a = x
    if type(a) == int:
      while  a > 1:
        a = a / 10
        counter += 1
      print(f"{x} has {counter} digits.")
      return None
  except:
    print ("Invalid input.")
  

def main():
 # remove the following line and write your program here
  # x = num_digits(x)
  # print(f"{x} has {num_digits}")
  num_digits()
  

# This is needed for the tests. This is now the first bit of code Python will run.
if __name__ == "__main__":
 main() # calls the main function
