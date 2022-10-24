'''Exercise 3.3'''

prompt = float(input("Enter 1 to convert Celsius to Fahrenheit or 2 to convert Fahrenheit to Celsius:\n"))

if prompt < 1 or prompt > 2:
  print("ERROR: Invalid option")

if prompt == 1:
  celsius = float(input("Please enter the temperature in Celsius:\n"))
  if celsius < 0:
    print("ERROR: You must enter a value of 0 or greater.")
  else:
    fahrenheit = (9/5) * celsius + 32
    print(f"{celsius} Celsius is equivalent to {fahrenheit} Fahrenheit.")

if prompt == 2:
  fahrenheit = float(input("Please enter the temperature in Fahrenheit:\n"))
  if fahrenheit < 0:
    print("ERROR: You must enter a value of 0 or greater.")
  else:
    celsius = (5/9) * (fahrenheit - 32)
    print(f"{fahrenheit} Fahrenheit is equivalent to {celsius} Celsius.")