def power_multiple_base_case(exponent, base):
    if base == 0:
        return 1
    elif base == 1:
        return base
    else:
        return exponent * power_multiple_base_case(exponent, (base-1))

# base cases
print power_multiple_base_case(3, 0)
print power_multiple_base_case(4, 1)

# general cases
print power_multiple_base_case(4, 8)
print power_multiple_base_case(2, 3)
