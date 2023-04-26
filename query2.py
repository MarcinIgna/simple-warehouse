from classes import Employee, User
from loader import Loader

# personnel
personnel = Loader(model="personnel").Employee_Unpacked


# items
x = Loader(model="stock")
stock = x.objects

# print(stock[1].stock)
warehouse_functions = stock[1]



# checking if user or employee and greeing with no password
name = "Jeremy".capitalize()
password = "copper"
employee = Employee(name, password)
user = User(name)
after_check = employee.get_user_name(personnel)
# options for user and for employee
option = employee.option_check(after_check)
history = 0
# if user will pick 1 showing all items by warehouses
if option == "1":
    history += 1
    for warehouse in stock:
        print("Warehouse: ", warehouse.id)
        print(warehouse.show_all())


# if user will pick 2 "search and buy* still need to be done
elif option == "2":
    item_search = input(
        "Input item that you are looking for: "
    ).lower()  # output tells u date nr warehouse.
    warehouse_functions.search_by_warehouse(item_search, x)
    history += 1
    while True:
        order = input("Do you wanna order? Y or N").lower()
        if order == "y":
            ammount = input("How many do you want to order?")
            if ammount.isdigit():
                employee.order(item_search, ammount)
            else:
                print("Wrong input")

        elif order == "n":
            break
        else:
            print("Wrong input")


elif option == "3":  # if user will pick 3 "search by category"
    history += 1
    warehouse_functions.print_search_by_cat(stock)


# if user will pick 4
elif option == "4":
    pass
# Else, if they pick something else
else:
    print("*" * 50)
    print(f"'{option}' is not a valid operation.")
    print("*" * 50)
# Print user history
# Thank the employee/user for the visit
if after_check:
    employee.bye(history)
else:
    user.bye()

