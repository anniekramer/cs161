def triangle(rows):
    if rows == 0:
        return 0
    else:
        return rows + triangle(rows-1)

print triangle(3)
print triangle(2)
print triangle(1)
print triangle(500)

# base case here
print triangle(0)
