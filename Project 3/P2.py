def RecursiveBinarySearch(Array: list, Target: int, Start_Index: int, End_Index:int) -> int:
    if Start_Index > End_Index:
        return -1

    Mid_Index = (Start_Index + End_Index) // 2
    Mid_Element = Array[Mid_Index]

    if Mid_Element == Target:
        return Mid_Index

    index_left_side = RecursiveBinarySearch(Array, Target, Start_Index, Mid_Index - 1)
    index_right_side = RecursiveBinarySearch(Array, Target, Mid_Index + 1, End_Index)

    return max(index_left_side, index_right_side)


def rotated_array_search(input_list: list, number: int) -> int:
    """
    Find the index by searching in a rotated sorted array
    Args:
       input_list(array): Input array to search
       number (int): target to search
    Returns:
       int: Index or -1
    """

    return RecursiveBinarySearch(Array=input_list, Target=number, Start_Index=0, End_Index=len(input_list) - 1)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
# Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
# Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
# Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
# Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
# Pass


print('\nEdge Cases:')
test_function([[], -1])
# Pass
test_function([[1], 0])
# Pass
