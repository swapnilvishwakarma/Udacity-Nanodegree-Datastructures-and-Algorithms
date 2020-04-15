def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.
    Args:
       input_list(list): List to be sorted
    """
    i_zero = 0
    i_one = 0
    i_two = len(input_list) - 1

    while i_one <= i_two:
        if input_list[i_one] == 0:
            input_list[i_one] = input_list[i_zero]
            input_list[i_zero] = 0
            i_zero += 1
            i_one += 1

        elif input_list[i_one] == 2:
            temp_val = input_list[i_two]
            input_list[i_two] = 2
            input_list[i_one] = temp_val
            i_two -= 1

        else:
            i_one += 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
print('\n')

print('Edge Cases:')
test_function([0, 1, 1, 0, 1])
test_function([0, 0, 0])
test_function([])
