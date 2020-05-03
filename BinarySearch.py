def binary_search(input_array, value):
    first = 0
    last = len(input_array) - 1
    found = False
    while(first<=last and not found):
        mid = (first+last)//2
        if input_array[mid] == value:
            found = True
        elif input_array[mid] > value:
            last = mid - 1
        else:
            first = mid + 1
    if found == True:
        return "Matched"
    else:
        return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))