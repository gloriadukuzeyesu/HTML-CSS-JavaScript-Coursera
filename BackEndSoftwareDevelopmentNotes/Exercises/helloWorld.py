
with open('Exercises/names.txt', 'r') as file:
  lines = file.read()
print(lines)



my_ty = (2, 3)
print(my_ty)
def divide(x,y):
    return x / y

try:
    res = divide(20, 0)
    print(res)
except ZeroDivisionError as e:
    print("Not possible: ", e)


list_a = [1,2]

y = list_a[1]
list_a.extend(list_a)
list_a.append(10)

print("List: ", list_a, " ", y)

exit(0)


menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee', 
        "price": 2.50},
    3: {"name": 'cake', 
        "price": 2.79},
    4: {"name": 'soup', 
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}

order = [
    {'item': 'Product A', 'price': 10.99},

    {'item': 'Product B', 'price': 5.49},
  
]

# print(type(menu.values()))

names = []
total = 0

for items in menu:
    dic = menu.get(items)
    names.append(dic.get("name"))
    total += dic.get("price")


print(names)
print(round(total, 2))





# print(type(order))








