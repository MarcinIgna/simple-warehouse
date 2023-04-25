from data import stock
from collections import Counter
from datetime import datetime
from classes import Employee, User
from classes import Item




def get_user_name(name, personnel):
    for employee in personnel:
        if employee._name == name:
            return employee
        for i in employee.head_of:
            if i["user_name"] == name:
                return i
    return None

def greet_user(name,user_name):
    if user_name:
        user_name.greet()
        # for x in user_name.head_off:
        #     if x["user_name"] == name:
        #         x.gr

    # else:
    #     User.greet(name)



def get_selected_operation(user_name):
    if user_name:
        print("What would you like to do?\n1. List items by warehouse\n2. Search an item and place an order\n3. Browse by category\n4. Quit")
        choice = input("Pick a number: ")
        return choice
    else:
        print("\n1. List items by warehouse\n4. Quit")
        while True:
            choice = input("Pick a number: ")
            if choice == "1" or choice == "4":
                return choice
            else:
                print("Sorry, pick only from 1 or 4")


def list_items_by_warehouse(stock):
    for i in stock:
        print("Warehouse: ", i.id)
        print(i.show_all())


def search_item(stock):
    while True:
        item = input("Input item that you are looking for: ").lower()
        sume_of_items = 0
        list_of_items = []
        dict_of_items = {}
        x = stock.objects
        for warehouse in x:
            for item_ware in warehouse.stock:
                compare = f"{item_ware.state} {item_ware.category}".lower()
                if compare == item:
                    sume_of_items += 1
                    list_of_items.append(warehouse)
                    ware_id = warehouse.id
                    if ware_id in dict_of_items:
                        dict_of_items[ware_id] += 1
                    else:
                        dict_of_items[ware_id] = 1

                    date = item_ware.date_of_stock
                    days = (datetime.now() - datetime.strptime(date, '%Y-%m-%d %H:%M:%S')).days
                    print(f'- Warehouse {ware_id} (in stock for {days} days)')

        if sume_of_items == 0:
            print(f"Sorry, we don't have that '{item}' in stock")
            continue
        else:
            print(f"Maximum availability: {max(dict_of_items.values())} in Warehouse {max(dict_of_items.items(), key=lambda x: x[1])[0]}")
        print(f"Ammount of items {sume_of_items}")


        return item, sume_of_items

def order(item, sume_of_items):
    while True:
        choice = input(f"Do you want to place an order?\n1.I wanna buy '{item}'\n2. I wanna look for another item.\n3. I wanna quit ")
        if choice == "1":
            amount = int(input(f"How many items do you want to order? Max available {sume_of_items} "))
            if amount > sume_of_items:
                print("*" * 50)
                print(f"There are not this many available. The maximum amount that can be ordered is {sume_of_items}")
                print("*" * 50)
                a_max = input("Would you like to order the maximum available?\n1. Yes and I wanna look for another.\n2. Yes and I wanna quit.\n3. Quit. ")
                if a_max == "1":
                    print(f"Thank you for your order of {sume_of_items} {item}")
                    return item, sume_of_items
                elif a_max == "2":
                    print(f"Thank you for your order of {sume_of_items} {item}")
                    return item, sume_of_items
                elif a_max == "3":
                    print("Quitting...")
                    return None, None
                else:
                    print(f"{a_max} is not a valid operation.")
            else:
                print(f"Thank you for your order of {amount} {item}")
                return item, amount
        elif choice == "2":
            return None, None
        elif choice == "3":
            print("Quitting...")
            return None, None
        else:
            print(f"{choice} is not a valid operation.")


def browse_by_category(stock):
    list_categories = []
    for i in stock:
        for j in i.stock:
            list_categories.append(j.category)
        cat_counter = Counter(list_categories)
    for i, (key, val) in enumerate(cat_counter.items()):
        print(f"{i + 1}. {key} ({val})")
    cat = int(input("Type the number of the category to browse: "))
    if cat > 26 or cat < 0:
        print("*" * 50)
        print(f"'{cat}' is not a valid operation.")
        print("*" * 50)
    else:
        for i in stock:
            for j in i.stock:
                if list_categories[cat - 1] == j.category:
                    print(f"- {j.state} {j.category}, Warehouse {i.id}")
def print_user_history(name, user_history):
    print(f"Thank you for your visit, {name}!")
    if len(user_history) == 0:
        print("You did not perform any operations in this session.")
    else:
        print("In this session you have:")
        for i, operation in enumerate(user_history):
            print(f"\t{i+1}. {operation}")