from data import personnel as employees
from data import stock as items
from loader import Loader
from collections import Counter

from datetime import datetime


class Item:
    def __init__(self, state, category, warehouse, date_of_stock):
        self.state = state
        self.category = category
        self.date_of_stock = date_of_stock
        self.warehouse = warehouse

    def __str__(self):
        item = self.state + " " + self.category
        return f"{item}"


class Warehouse:
    def __init__(self, warehouse_id):
        self.id = warehouse_id
        self.stock = []

    def occupancy(self):  # all items in stock
        return len(self.stock)

    def add_item(self, item=Item):
        self.stock.append(item)

    def dell_item(self, item=Item):
        self.stock.remove(item)

    def show_all(self):
        for i in self.stock:
            print(i)
        return ""

    def print_search_by_cat(
        self, warehouses_stock
    ):  # this counting in all warehouses ant printing
        x = Counter()
        for nr_warehouse in range(len(warehouses_stock)):
            x += warehouses_stock[nr_warehouse].search_by_category()
        for i, (key, val) in enumerate(x.items()):
            print(f"{i + 1}. {key} ({val})")

    def search_by_category(self):  # this returning counter object of one warehouse
        list_categories = []

        for item in self.stock:
            list_categories.append(item.category)
        cat_counter = Counter(list_categories)

        return cat_counter

        # Category
        # cat = int(input("Type the number of the category to browse: "))
        # if cat > 26 or cat < 0:
        #     print("*" * 50)
        #     print(f"'{cat}' is not a valid operation.")
        #     print("*" * 50)
        # else:
        #     for item in self.stock:
        #         if list_categories[cat - 1] == item.category:
        #             print(f"- {item.state} {item.category}, Warehouse {item.warehouse}")

    def search_by_warehouse(self, item, stock):
        """
        This function is searching for item in all warehouses and printing
        how many items are in stock, in which warehouse and for how long.
        """
        sume_of_items = 0
        list_of_warehouses = []
        dict_of_items = {}
        list_of_items = []
        x = stock.objects
        for warehouse in x:
            for item_ware in warehouse.stock:
                compare = f"{item_ware.state} {item_ware.category}".lower()
                if compare == item:
                    sume_of_items += 1
                    list_of_items.append(compare)
                    list_of_warehouses.append(warehouse)
                    ware_id = warehouse.id
                    if ware_id in dict_of_items:
                        dict_of_items[ware_id] += 1
                    else:
                        dict_of_items[ware_id] = 1

                    date = item_ware.date_of_stock
                    days = (
                        datetime.now() - datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
                    ).days
                    print(f"- Warehouse {ware_id} (in stock for {days} days)")

        if sume_of_items == 0:
            print(f"Sorry, we don't have that '{item}' in stock")

        else:
            print(
                f"Maximum availability: {max(dict_of_items.values())} in Warehouse {max(dict_of_items.items(), key=lambda x: x[1])[0]}"
            )
        print(f"Ammount of items {sume_of_items}")
        return list_of_items

    def search(self, search_term):
        # return [item for item in self.stock if search_term in item.name]
        matches = []
        for i in self.stock:
            compare = f"{i.state} {i.category}".lower()
            print(i.state.lower(), i.category.lower(), "in loop")
            if search_term == compare:
                matches.append(i)

        return matches


class User:
    def __init__(self, name: str = "Anonymous", is_authenticated: bool = False):
        self._name = name
        self.is_authenticated = is_authenticated

    def authenticate(self, password: str):
        return False

    def is_named(self, name):
        if self._name == name:
            return True
        return False

    def greet(self):
        print(
            f"Hello, {self._name}!\nWelcome to our Warehouse Database.\nIf you don't find what you are looking for,\nplease ask one of our staff members to assist you."
        )

    def bye(self):
        print(f"Goodbye, {self._name}!")


class Employee(User):
    def __init__(
        self,
        user_name: str,
        password: str,
        is_authenticated: bool = False,
        head_of: list = [],
    ):
        super().__init__(user_name, is_authenticated)
        self.__password = password
        self.head_of = head_of
        # self.user_name = user_name

    def get_user_name(self, personnel):  # authenticate by name
        for employee in range(len(personnel)):
            if personnel[employee]._name == self._name:
                # print(employee)
                self.greet()
                return True
            super().greet()
            return False

    def authenticate(self, password: str):
        if self.__password == password:
            return True
        return False

    def option_check(self, after_check):  # optins for employee and user
        if after_check:
            print(
                "What would you like to do?\n1. List items by warehouse\n2. Search an item and place an order\n3. Browse by category\n4. Quit"
            )
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

    def order(self, item: Item, amount: int):
        print(f"Ordering {amount} of {item}...")

    def greet(self):
        print(
            f"Hello, {self._name}!\nIf you experience a problem with the system,\nplease contact technical support."
        )

    def bye(self, actions = 0):
        super().bye()
        print(f"You have performed {actions} actions.")
