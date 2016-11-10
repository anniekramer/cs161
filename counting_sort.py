def counting_sort(list, k):
    counter = [0] * (k + 1)
    for i in list:
        counter[i] += 1

    index = 0
    for i in range(len(counter)):
        while counter[i] > 0:
            list[index] = i
            index += 1
            counter[i] -= 1

    print list
    print "Done!"

test_array = [5,2,5,6,4,3,6]
test_array_range = len(test_array)

counting_sort(test_array, test_array_range)
