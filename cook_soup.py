
import soup
import webbrowser



# iNGREDIENTS
class CookSoup():
    def __init__(self,*args) -> None:
        self.items = args
        

    def cook(self):
        #abstract the names of the ingredients into a list
        ing = []

        for item in self.items:
            ing.append(item.name)

        # create a search url for the soup

        search_url = ' '.join(str(x) for x in ing)
        search_url = "Soup recipe for ingredients: " + search_url


        base_url = "http://www.google.com/search?q="

        url = base_url + search_url
        web_browser = webbrowser.open(url)



if __name__ == "__main__":
    #Ingredients

    flour = soup.Ingredient("flour",2)
    sugar = soup.Spice("sugar",2,"chilli")
    paprica = soup.Spice("sugar",2,"sweet")
    eggs = soup.Ingredient("Egg",4)



    soup = CookSoup(flour,sugar,eggs)

    soup.cook()


