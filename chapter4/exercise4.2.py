'''Exercise 4.2'''

speed = int(input("What is the speed of the vehicle in mph?\n"))

hours = int(input("How many hours has it travelled?\n"))
print("")

count = 0
print("Hour | Distance Travelled")
print("-----------------------\n")
for i in range (hours):
  count += 1
  print(f"{count}    | {speed * count}")