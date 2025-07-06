from expense import Expense


def main():
  print(f"Running Expense Tracker")

  # Get use input for expense
  get_user_expense()

  #Write their expense in a file
  save_expense_to_file()

  #Read file and summarize expenses
  summarize_user_expense()


def get_user_expense():
  print(f"Getting User Expense")
  
  expense_name = input("Enter expense name: ")
  expense_amount = float(input("Enter expense amount:"))
  print(f"You've entered {expense_name}, {expense_amount}")

  expense_categories = {
    "Home",
    "Car",
    "Savings",
    "Grocery",
    "Remittance",
    "Misc.",
  }

  while True:
    print("Select a category:")
    for i, category_name in enumerate(expense_categories):
      print(f"  {i + 1}. {category_name}")
  
    value_range = f"[1 - {len(expense_categories)}]"
    selected_index = int(input(f"Enter a catagory number {value_range}: ")) - 1

    if selected_index in range(len(expense_categories)):     
      selected_category = expense_categories[selected_index]
      new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
      return
    else:
      print("Invalid category. Try again!")
    
def save_expense_to_file():
  print(f"Saving User Expense")

def summarize_user_expense():
  print(f"Summarizing User Expense")



if __name__ == "__main__":
  main()

