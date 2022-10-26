'''Exercise 4.4'''

a = int(input("Please enter the size (no of rows) of the triangle you wish to display:"))

a += 1

star = "*"
counter = 0

for i in range (a):
  print (star * i)
