# Given numbers from 1 to N you have to place a sign (+/-) in front of each number such that the sum of the entire series becomes 0. If its impossible to get a sum as 0 find the minimum positive number that the series will converge to.

# N = 6

def minimizeSum(N):
    if N == 1:
        return 1
    if N == 2 or N == 3:
        return 0
    if N % 2 == 0:
        if (N // 2) % 2 == 0:
            return 0
        else:
            return 1
    else:
        rem_length = N - 1
        if (rem_length // 2) % 2 == 0:
            return 1
        else:
            return 0

print(1, minimizeSum(1))
print(2, minimizeSum(2))
print(3, minimizeSum(3))
print(4, minimizeSum(4))
print(5, minimizeSum(5))
print(6, minimizeSum(6))
print(7, minimizeSum(7))
print(8, minimizeSum(8))
print(9, minimizeSum(9))
# 1 = 1
# 1,2 = 1
# 1,2,3 = 0
# 1,2,3,4 = 0
# 1,2,3,4,5 = 1
# 1,2,3,4,5,6 = 1
# 1,2,3,4,5,6,7 = 0
# 1,2,3,4,5,6,7,8 = 0
# 1, 2,3, 4,5, 6,7, 8,9 = 1