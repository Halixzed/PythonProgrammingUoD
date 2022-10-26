'''Exercise 4.1'''

print("This program calculates the average of a series of numbers entered.")
count = 0
num = float(input("Please enter a number. Enter 0 to stop\n"))
sum = 0

while num != 0:
  sum += num
  count += 1
  num = float(input("Please enter a number. Enter 0 to stop\n"))
if count == 0:
  print("No numbers entered.")
else:
  print(f"The average of the numbers entered is {sum/count}")
  