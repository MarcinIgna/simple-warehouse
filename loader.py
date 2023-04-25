"""Data loader."""

from data import personnel as employees
from data import stock as items


class MissingClassError(Exception):
    """Missing class exception."""

    def __init__(self, name=None, message="Missing class."):
        """Constructor."""
        if name:
            self.class_name = name
            self.message = f"Missing class {name}."
        super().__init__(self.message)


class MissingArgument(Exception):
    pass


class Loader:
    """Main data loader class."""

    model = None
    objects = None
    Employee_Unpacked = [] #created new empty property

    def __init__(self, *args, **kwargs):
        """Constructor."""
        if "model" not in kwargs:
            raise MissingArgument("The loader requires a `model` keyword argument to work.")
        self.model = kwargs["model"]
        self.parse()
        self.__unpacked() #Initialize function when class object is created
                          #Use below in query to create unpacked dataset
                             #personnel = Loader(model='personnel')
                             #personnel_unpacked = personnel.Employee_Unpacked


    def parse(self):
        """Instantiate objects from the data."""
        if self.model == "personnel":
            self.objects = self.__parse_personnel()
        if self.model == "stock":
            self.objects = self.__parse_stock()

    def __load_class(self, name):
        """Return a class."""
        classes = __import__("classes")
        if not hasattr(classes, name):
            raise MissingClassError(name)
        return getattr(classes, name)

    def __parse_personnel(self):
        """Parse the personnel list."""
        Employee = self.__load_class("Employee")

        return [Employee(**employee) for employee in employees]

    def __unpacked(self): #new function for unpacking objects
        """Parse the personnel list."""
        Employee2 = self.__load_class("Employee")

        for i in employees:
            if 'head_of' not in i:
                self.Employee_Unpacked.append(Employee2(i['user_name'], i['password']))
            else:
                self.Employee_Unpacked.append(Employee2(i['user_name'], i['password']))
                for j in i['head_of']:
                    if 'head_of' not in j:
                        self.Employee_Unpacked.append(Employee2(j['user_name'], j['password']))
                    else:
                        self.Employee_Unpacked.append(Employee2(j['user_name'], j['password']))
                        for k in j['head_of']:
                            if 'head_of' not in k:
                                self.Employee_Unpacked.append(Employee2(k['user_name'], k['password']))
                            else:
                                self.Employee_Unpacked.append(Employee2(k['user_name'], k['password']))
                                for t in k['head_of']:
                                    self.Employee_Unpacked.append(Employee2(t['user_name'], t['password']))


    def __parse_stock(self):
        """Parse the stock."""
        Item = self.__load_class("Item")
        Warehouse = self.__load_class("Warehouse")
        warehouses = {}
        for item in items:
            warehouse_id = str(item["warehouse"])
            if warehouse_id not in warehouses.keys():
                warehouses[warehouse_id] = Warehouse(warehouse_id)
            warehouses[warehouse_id].add_item(Item(**item))
        return list(warehouses.values())

    def __iter__(self, *args, **kwargs):
        """Iterate through the objects."""
        yield from self.objects