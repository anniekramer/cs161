def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, (n-1))

# base case
print power(3, 0)

# general cases
print power(4, 8)
print power(2, 3)