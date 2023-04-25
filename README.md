# Simple warehouse
This code is a simple inventory management system for a warehouse. 

## Project Overview
This project contains four classes, `Employee`, `User`, `Loader`, and `Warehouse`. The `Loader` class imports data from an external file and provides it to the program. The `Warehouse` class has functions for searching for items by category and by warehouse, and for ordering items.

## Usage

When the program is running, it will greet the user and ask for their name. If the name belongs to an employee in the personnel file, the program will ask for their password. Otherwise, it will greet the user and continue as a regular user.

After checking whether the user is an employee or a regular user, the program will present a list of options for the user to choose from. Depending on their choice, the program will perform different tasks.

If the user chooses option 1, the program will show all the items available in the warehouse. If they choose option 2, they will be prompted to enter the name of an item they are looking for. The program will then search for the item in the warehouse and display which warehouse it can be found in. The user will be asked if they want to order the item, and if they do, they will be prompted for the quantity they wish to order.

If the user chooses option 3, the program will show all the categories available in the warehouse. If they choose a category, the program will show all the items in that category.

If the user chooses option 4, the program will exit.

After the user finishes interacting with the program, the program will print a history of the user's choices and say goodbye.

## Credits

This project was created by Me as part of a Python course. The project was based on a template provided by the course instructors. 
