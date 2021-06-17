import beverage as b


class Vendingmachine:
    def __init__(self, name, stock):
        """
        taking a string, an array of Beverage instances as parameters, assign its value to a name attribute and a stock attribute.
        """
        self.name = name
        self.stock = stock

    def __str__(self):
        """
        return its name attributes in the format.
        <name attribute> the vending machine
        """
        return f"{self.name} the vending machine"

    def sell(self, beverage_name):
        """
        taking a string as a parameter, print a message of your choice.
        the message differ when there is a Beverage instance named same as product_name in the stock, or not.
        """
        dict = {}
        for i in self.stock:
            dict[i.name] = i.price

        if beverage_name in dict:
            print("Here is your " + beverage_name + "!")
        else:
            print("Sorry! I do not have " + beverage_name + "...")

    def ask(self):
        """
        print a message to ask the beverage name,
        store the user input,
        then call sell method with the users input as parameter.
        """
        bname = input("Hello, what would you like?\n")
        self.sell(beverage_name=bname)
