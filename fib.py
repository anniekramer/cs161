def fib(n):
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    else: 
        return fib(n-1) + fib(n-2)

# test cases
print F(0)
print F(1)
print F(24)
print F(997)

# this exceeds maximum recursion depth
# to investigate:
# stack overflow, tail recursion, unbridled recursion
# print F(222222)