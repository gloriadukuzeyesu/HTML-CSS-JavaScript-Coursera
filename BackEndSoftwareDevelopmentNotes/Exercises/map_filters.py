menu = {"espresso", "mocha", "latte", "cappuchino", "americano","cortado"}

def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee
    
map_coffee = map(find_coffee, menu)
for item in map_coffee:
    print(item)

print()

filter_coffee = filter(find_coffee, menu)
for item in filter_coffee:
    print(item)
