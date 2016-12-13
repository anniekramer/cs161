def value_in_list(array, n, i):
    if array[i] == n:
        return true
    elif n == (len(array) - 1):
        return false
    else:
        return value_in_list(array, n, (i+1))

a = [3,4,5,6,7,8,9]

print value_in_list(a, 2, 2)