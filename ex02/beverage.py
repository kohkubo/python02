import product as pd


class Beverage(pd.Product):
    def __init__(self, name, price, description, temperature):
        """
        assign its values to name, price, description, temperature attribute, using super(),
        """
        super().__init__(name, price, description)
        self.temperature = temperature

    def print_attr(self):
        """
        return its name, price, description and temperature attributes in the format.
        name : <name attribute>
        price : <price attribute limited to two decimal points>
        description : <description attribute>
        temperature : <temperature attribute>
        """
        return f"name : {self.name}\nprice : {self.price}\ndescription : {self.description}\ntemperature : {self.temperature}"
