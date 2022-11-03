'''Exercise 5.3'''

def num_digits(x):
     # remove the following line and write the function here
  counter = 0
  q = x
  if q < 0:
    q = q * -1
    
  while  q >= 1:
    q = q / 10
    counter += 1
  return counter
  

def main():
 # remove the following line and write your program here
  # x = num_digits(x)
  # print(f"{x} has {num_digits}")
  try:
    x = int(input("Please enter a positive whole number:\n"))
    if type(x) == int:
      if x != 0:
        if num_digits(x) > 1:
          print (f"{x} has {num_digits(x)} digits.")
        else:
          print (f"{x} has {num_digits(x)} digit.")
      if x == 0:
        print("Invalid input.")
          
  except:
    print ("Invalid input.")
    
    
  

# This is needed for the tests. This is now the first bit of code Python will run.
if __name__ == "__main__":
 main() # calls the main function
