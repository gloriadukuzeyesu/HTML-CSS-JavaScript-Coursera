
def access_element(arr, index):
    return arr[index]

print(access_element([1,2,3], 1))

def linear_search(arr, target):
    for item in arr:
        if item == target:
            return True
        
    return False

print(linear_search([1,2,3,4,5], 8))

# buble sort is quadratic time complex
# quadratic alogarithm grows with the the square of the input size

def buble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)

buble_sort([3,6,4,8,1,0,5])
# 3,4,6,1,5,1


# O (log n) 
def binary_seach(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
        
    return -1


print(binary_seach([3,4,6,8,9,10], 4))

