import product as pd


class Beverage(pd.Product):
    def __init__(self, name, price, description, temperature):
        """
        assign its values to name, price, description, temperature attribute, using super(),
        """
        super(Beverage, self).__init__(name, price, description)
        self.temperature = temperature

    def print_attr(self):
        """
        return its name, price, description and temperature attributes in the format.
        name : <name attribute>
        price : <price attribute limited to two decimal points>
        description : <description attribute>
        temperature : <temperature attribute>
        """
        return "name : {0}\nprice : {1}\ndescription : {2}\ntemperature : {3}".format(
            self.name, self.price, self.description, self.temperature
        )
