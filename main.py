import requests
from pprint import pprint
import webbrowser

class Ingredient:
    """Models a food item used as an ingredient."""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def expire(self):
        """Expires the ingredient."""
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name

    def __add__(self, other):
        """Combines two ingredients."""
        new_name = self.name + other.name
        if self.amount < other.amount:
            new_amount = self.amount
        elif self.amount > other.amount:
            new_amount = other.amount
        elif self.amount == other.amount:
            new_amount = other.amount

        return Ingredient(name=new_name, amount=new_amount)
    
    def __str__(self):
        return f"{self.name} ({self.amount})"
    
    def __repr__(self):
        return f"Ingredient(name={self.name}, amount={self.amount})"

    def get_info(self):

        base_url = "https://en.wikipedia.org/wiki"
        complete_url = base_url + "/" + self.name

        web = webbrowser.open_new_tab(complete_url)

    
carrot = Ingredient("carrot",10)
sugar = Ingredient("sugar",8)

sugar.get_info()



