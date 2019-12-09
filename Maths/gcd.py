def gcd(a,b):
    if a == 0:
        return b
    if a == b:
        return a
    return gcd(b%a, a)

print(gcd(60,25))
