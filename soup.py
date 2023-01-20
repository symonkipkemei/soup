import webbrowser




class Ingredient:
    """Models a food item used as an ingredient."
    """
    

    def __init__(self, name:str, amount:int):
        """Creates instance variables

        Args:
            name (str): name of object
            amount (int): amount of object
        """

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
    
    def details(self):
        base_url = "https://en.wikipedia.org/wiki"
        name_url = str.capitalize(self.name)
        url = base_url + "/" + name_url
        web_browser = webbrowser.open(url)

    
    def __str__(self):
        return f"{self.name} ({self.amount})"
    
    def __repr__(self):
        return f"Ingredient(name={self.name}, amount={self.amount})"



class Spice(Ingredient):
    "Models a spice to flavor your food"

    def grind(self):
        print(f"You have now {self.amount} of ground {self.name}")

    def expire(self):
        print(f" Your {self.name} has expired. It's probably still good")
        self.name = "old" + self.name
        
    pass

if __name__ == "__main__":
    p = Ingredient("PEAS", 20)
    print(p)

    s = Spice("salt",20)


    s.expire()
    s.grind()

    

    print(s)

    s.details()

    s.expire()
    print(s.name)







