import math

input_arr = [2, 42, 82, 122, 162, 202, 242, 282, 322, 362]
print(input_arr)
print("*****")
low = 0
high = len(input_arr) - 1
target = int(input())
found_element = False
closest = math.inf
while low <= high:
    mid = (low + high + 1) // 2
    print(low, high, mid, input_arr[mid])
    if abs(target - input_arr[mid]) < abs(target - closest):
        closest = input_arr[mid]
    if input_arr[mid] == target:
        found_element = True
        break
    elif input_arr[mid] < target:
        low =  mid + 1
    else:
        high = mid - 1
if found_element:
    print("Found Element: ", input_arr[mid])
else:
    print("Closest Element is: ", closest)
