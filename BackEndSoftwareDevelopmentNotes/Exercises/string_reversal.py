# 1st method: slice function
# str[start:stop:step]

trial = "gloria"
new_trial = trial[::-1]
print(new_trial)

# recursion

def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0]

string_reversed = string_reverse(trial)
print(string_reversed)
