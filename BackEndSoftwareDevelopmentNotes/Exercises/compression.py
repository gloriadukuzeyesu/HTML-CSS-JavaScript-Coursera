
# Set comprehension
set_a = { x for x in range(10) if x % 2 == 0}
# print(set_a)

data = [2,3,5,7,11,13,17,19,23,29,31]

gen_obj = (x for x in data)
print(gen_obj)
for x in gen_obj:
    print(x, end = " ")


# dictionary comprehesion 

# Using range() function and no input list
using_range = {x : x * 2 for x in range(12)}
print(using_range)
print()
# using one list to make a dictionary 
numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

numdict = { x : x ** 2 for x in numbers}
print(numdict)

print()
# using two lists
month_dict = { key : value for key, value in zip (numbers, months)}
print(month_dict)

# List comprehension
data = [2,3,4,5,5,9, 12, 15]

data_copy = [ x for x in data if x % 2 == 0]
print(data)
print (data_copy)
nines = [x for x in range(len(data)) if x % 2 == 0]
print (nines)


