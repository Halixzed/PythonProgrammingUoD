import json


def add_item(menu_dict, name, price):
  """ Adds a new item to the menu"""
  next_id = menu_dict.get("next_id")
  update = {
    str(next_id) : {
      "Name": name,
      "Price": float(price)
    }
  }
  next_id += 1
  menu_dict["next_id"] = next_id
  menu_dict["menu"].update(update)
  return menu_dict
  


def load(filename):
  """ loads the file into a dictionary and returns dictionary"""
  with open(filename, "r") as f:
    menu_dict = json.load(f)
    return(menu_dict)
  


def save(filename, menu_dict):
  """ save out the menu to the filename"""
  with open(filename, "w") as out:
    json.dump(menu_dict, out)


def list_options():
  print("Option 1: List Menu")
  print("Option 2: Add Menu Item")
  print("Option 3: Quit")


def print_menu(menu_dict):
  print("\nMENU")
  print("----\n")
  for key, value in menu_dict["menu"].items():
    print(f"Item {key}\n")
    print(f"Name: {value['Name']}")
    print(f"Price: {value['Price']}\n")


def main():
  filename = "menu.json"
  menu = load(filename)
  list_options()
  option = input("\nPlease select an option:\n")
  while option != "3":
    if option == "1":
      print_menu(menu)
    elif option == "2":
      name = input("\nPlease enter a name:\n")
      price = input("\nPlease enter a price:\n")
      add_item(menu, name, price)
      save(filename, menu)
    option = input("\nPlease select an option:\n")


if __name__ == "__main__":
  main()