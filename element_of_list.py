def element_of_list(elem, list):
    if len(list) == 0:
        return False
    if list[0] == elem:
        return list
    return element_of_list(elem, list[1:])

test_list = [1,2,3,4,5,6,7,8,9]

print element_of_list(2, test_list)
print element_of_list(222, test_list)