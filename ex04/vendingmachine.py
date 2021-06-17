import beverage as b


class Vendingmachine:
    def __init__(self, name, greeting, stock):
        """
        taking 2 string, an array (a Beverage instance, integer) as parameters,
        assign its value to a name attribute, a greeting attribute and a stock attribute.
        """
        self.name = name
        self.greeting = greeting
        self.stock = stock


    def __str__(self):
        """
        return its name attributes in the format.
        <name attribute> the vending machine
        """
        return "{0}\n".format(self.name)

    def sell(self, beverage_name):
        """
        taking a string as a parameter, print a message of your choice.
        the message differ when there is a Beverage instance
        named same as product_name in the stock, or not.
        """
        self.beverage_name = beverage_name
        if (self.beverage_name == self.name and self.stock != 0):
            print("Here is your " + self.beverage_name + "!")

        else:
            print("Sorry! I do not have " + self.beverage_name + "...")

    def ask(self):
        """
        print a message to ask the beverage name,
        store the user input,
        then call sell method with the users input as parameter.
        """
        bname = input("Hello, what would you like?\n")
        self.sell(beverage_name=bname)

    def add_stock(self, beverage_name, number):
        """
        taking a string and integer as parameters,
        increase the number of stocks
        when the Beverage instance with the same name as beverage_name exists in the stock.
        if not, create a new Beverage instance and add it into its stock with the number
        """
        self.beverage_add = beverage_name
        self.number = number
        if (self.name == self.beverage_add):
            self.stock += self.number
        else:
            setattr(Vendingmachine, "beverage_new", self.beverage_add)
            setattr(Vendingmachine, "stock_new", self.number)