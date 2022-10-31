'''Exercise 5.1'''

def calc_retail_price(wholesale = 0.00, markup = 0):
     # remove the following line and write your function here
  retail = ((markup / 100) * wholesale) + wholesale
  return retail

def main():
 # remove the following line and write your main program here
  #main_retail = calc_retail_price(5.00, 50)
  #round (main_retail, 2)
  a = float(input("Please enter a wholesale cost:\n"))
  b = float(input("Please enter a markup percentage:\n"))
  print (f"The retail price is £{calc_retail_price(a, b)}.")

  
# This is needed for the tests. This is now the first bit of code Python will run. 
# Please ask if you are curious, but it is enough to understand that this calls the main() function and runs whatever code you have in there.
if __name__ == "__main__":
 main() # calls the main function
 
 # uncomment the following lines to test calc_retail_price when you run the program.
 # you will need to comment out main() 
 # print(calc_retail_price(3.00, 100)) # should print 6.0
 # calc_retail_price(5.00, 50) # should print 7.5
#print(calc_retail_price(3.00, 100))
