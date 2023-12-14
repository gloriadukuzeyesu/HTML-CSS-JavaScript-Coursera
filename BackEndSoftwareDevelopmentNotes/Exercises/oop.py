class Recipe():
    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time
    
    def contents(self):
        print ("The " + self.dish + " has " + str(self.items) + \
               " and takes " + str(self.time) + " min to prepare")
        

pizza = Recipe( "Pizza", ["cheese", "bread", "tomatoes"], 45)
pasta = Recipe("Pasta", ["penne", "suace"], 55)

print(pizza.items)
print(pasta.items)


print(pizza.contents())
print(pasta.contents())


class MyFirstClass:
    index = ""
    def __init__(self, index = None) -> None:
        self.index = index

    def hand_list(self):
        print(self.index + " wrote the book: " + self.index)


hand = MyFirstClass("harry porter")
hand.hand_list()
hand1 = MyFirstClass(index = "hi")
hand1.hand_list()




                        

