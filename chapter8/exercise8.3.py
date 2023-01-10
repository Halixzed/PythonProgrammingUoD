import random
import math

def coin_tosses(n):
  tosses =[]
  for i in range(int(n)):
    tosses.append(random.randint(0, 1))
  #debugging
  print(tosses)
  return tosses

def count(tosses):
  countx = 0
  county = 0
  for x in tosses:
    if x == 1:
      countx += 1
    if x == 0:
      county += 1
  count_of_tosses = (countx, county)
  #new_tup = count_of_tosses[::-1]
  #debugging
  return count_of_tosses
  

def percentage(count_of_tosses):
  max_perc = 100.00
  no_of_tosses = count_of_tosses[0] + count_of_tosses[1]
  percentage_x = (count_of_tosses[0] / no_of_tosses) * max_perc
  percentage_y = (count_of_tosses[1] / no_of_tosses) * max_perc
  percentage_x = round(percentage_x, 2)
  percentage_y = round(percentage_y, 2)
  percentage_tosses = (percentage_x, percentage_y)
  return percentage_tosses
  

def main():
  x = input("How many coin tosses would you like to simulate?\n")
  tosses = coin_tosses(x)
  counts = count(tosses)
  print (f"\nNo. of Heads: {counts[1]}")
  print (f"No. of Tails: {counts[0]}")
  percent = percentage(counts)
  print (f"\n%   of Heads: {percent[1]}")
  print (f"%   of Tails: {percent[0]}")
  
  
if __name__ == "__main__":
  main()