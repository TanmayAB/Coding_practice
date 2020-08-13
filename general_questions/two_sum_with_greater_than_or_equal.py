

# list of numbers
# a+b >= 8



a = [1,2,4,7,6,3]

a.sort()

target = 8
result = []

i = 0
j = len(a) - 1

while i < j:
    while a[i] + a[j] >= target and i < j:
        result.append([a[i], a[j]])
        j -= 1
    i += 1
    j = len(a) - 1

print(result)

