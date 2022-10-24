'''Exercise 3.2'''

temperature_celsius = float(input("Please enter the temperature in Celsius:\n"))

Fahrenheit = (9/5) * temperature_celsius + 32

if temperature_celsius >= 0:
  print(f"{temperature_celsius} Celsius is equivalent to {round(Fahrenheit, 2)} Fahrenheit.")

elif temperature_celsius < 0:
  print("ERROR: You must enter a value of 0 or greater.")