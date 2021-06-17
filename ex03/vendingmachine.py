import random
import beverage as b


class Vendingmachine:
    def __init__(self, name, greeting, stock):
        """
        taking 2 string, an array of Beverage instances as parameters, assign its value to a name attribute, a greeting attribute and a stock attribute.
        """
        self.name = name
        self.greeting = greeting
        self.stock = stock

    def __str__(self):
        """
        return its name attributes in the format.
        <name attribute> the vending machine
        """
        return f"{self.name} the vending machine"

    def stock_dict(self, stock):
        dict = {}
        for i in stock:
            dict[i.name] = i.price
        return dict

    def greet(self):
        """
        print a greeting attribute of the instance.
        """
        print(self.greeting)

    def display(self):
        """
        show its lineup of stocks.
        """
        dict = {}
        for i in self.stock:
            print(f"{i.name}")

    def recommend(self):
        """
        choose a random instance from its stock,
        then print a recommendation sentence using the name attribute of the selected Beverage instance.
        """
        dict = self.stock_dict(self.stock)
        k, v = random.choice(list(dict.items()))
        print("I recommend...")
        print(f"{k} : the most popular drink!")

    def sell(self, beverage_name):
        """
        print a message of your choice.
        the message differ when there is a Beverage instance named same as beverage_name in the stock, or not call recommend method when the given beverage name is not found in its stock.
        """
        dict = self.stock_dict(self.stock)
        if beverage_name in dict:
            print("Here is your " + beverage_name + "!")
        else:
            print("Sorry! I do not have " + beverage_name + "...")
            self.recommend()

    def ask(self):
        """
        print a message to ask the beverage name,
        store the user input,
        then call sell method with the users input as parameter.
        """
        bname = input("Hello, what would you like?\n")
        self.sell(beverage_name=bname)
