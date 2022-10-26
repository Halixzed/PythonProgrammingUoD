'''Exercise 4.3'''

print ("This program calculates the largest number from a series of numbers entered.")

num = 1
num_list = []
i = 0

#input_bool = True

while num != 0:
  num = int(input("Please enter a number. Enter 0 to stop\n"))
  if num == 0 and len(num_list) == 0:
    print ("No numbers entered.")
  else:
    num_list.append(num)
    num_list.sort()
    if i in num_list:
      num_list.remove(i)
if len(num_list) != 0:
  print (f"The largest of the numbers entered is {max(num_list)}")