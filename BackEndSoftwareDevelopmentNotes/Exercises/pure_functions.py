my_list = [1,2,3]

def add_t_list(lst, item):
    nl = lst.copy()
    nl.append(item)
    return nl

new_list = add_t_list(my_list, 10)
print(my_list)
print(new_list)

# pure functions does not alter then global varibles

def factorial (n):
    if n <= 1:
        return 1
    return n * factorial( n - 1)

print(factorial(0))

