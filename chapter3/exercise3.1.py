'''Exercise 3.1'''

temperature_celsius = float(input("Please enter the temperature in Celsius:\n"))

Fahrenheit = (9/5) * temperature_celsius + 32

if temperature_celsius >= 0:
  print(f"{temperature_celsius} Celsius is equivalent to {Fahrenheit} Fahrenheit.")