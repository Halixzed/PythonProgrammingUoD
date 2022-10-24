'''Exercise 3.4'''

number_of_copies = float(input("Please enter the number of copies of the software you wish to purchase:\n"))

discount = 0
price = 99

if number_of_copies < 5:
  total_cost = (number_of_copies * 99)
  print(f"You have been given a 0% discount on the normal price of £99.\nThe total cost is £{total_cost:.2f}.")
  
if number_of_copies >= 5 and number_of_copies <= 9:
  total_cost = number_of_copies * price
  discount = total_cost * 0.1
  final = total_cost - discount
  print(f"You have been given a 10% discount on the normal price of £99.\nThe total cost is £{final:.2f}.")

if number_of_copies >= 10 and number_of_copies <= 19:
  total_cost = number_of_copies * price
  discount = total_cost * 0.2
  final = total_cost - discount
  print(f"You have been given a 20% discount on the normal price of £99.\nThe total cost is £{final:.2f}.")

if number_of_copies >= 20 and number_of_copies <= 49:
  total_cost = number_of_copies * price
  discount = total_cost * 0.3
  final = total_cost - discount
  print(f"You have been given a 30% discount on the normal price of £99.\nThe total cost is £{final:.2f}.")

if number_of_copies >= 50 and number_of_copies <= 99:
  total_cost = number_of_copies * price
  discount = total_cost * 0.4
  final = total_cost - discount
  print(f"You have been given a 40% discount on the normal price of £99.\nThe total cost is £{final:.2f}.")

if number_of_copies >= 100:
  total_cost = number_of_copies * price
  discount = total_cost * 0.5
  final = total_cost - discount
  print(f"You have been given a 50% discount on the normal price of £99.\nThe total cost is £{final:.2f}.")