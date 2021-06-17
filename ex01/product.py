class Product:
    def __init__(self, name, price, description):
        """
        assign its values to a name attribute and a price attribute.
        """
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        """
        return its name and description attributes in the format.
        <name attribute> : <description attribute>
        """
        return f"{self.name} : {self.description}"

    def print_attr(self):
        """
        return its name, price and description attributes in the format.
        name : <name attribute>
        price : <price attribute limited to two decimal points>
        description : <description attribute>
        """
        return f"name : {self.name}\nprice : {self.price}\ndescription : {self.description}"
