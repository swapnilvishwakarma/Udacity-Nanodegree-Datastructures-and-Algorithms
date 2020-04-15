def Rearrange_Digits(input_list: list, first_layer: bool = False) -> list:
    """
        Rearrange Array Elements so as to form two number such that their sum is maximum.
        Args:
           input_list(list): Input List
           first_layer(bool): placeholder to know if we are in the first layer of the recursion (special case)
        Returns:
           (int),(int): Two maximum sums
        """

    if len(input_list) <= 1:
        return input_list

    Mid = len(input_list) // 2
    Left = input_list[:Mid]
    Right = input_list[Mid:]

    Left = Rearrange_Digits(Left)
    Right = Rearrange_Digits(Right)

    return Merge(Left, Right, first_layer)


def Merge(left: list, right: list, first_layer: bool = False) -> list:
    Merged = []
    Left_Index = 0
    Right_Index = 0

    if first_layer:  # Special case for the last merging step
        num_max_left = ''
        num_max_right = ''
        num_to_left = True

        # Alternating between left and right indexes
        while Left_Index < len(left) and Right_Index < len(right):
            if left[Left_Index] > right[Right_Index]:
                if num_to_left:
                    num_max_left = str(right[Right_Index]) + num_max_left
                else:
                    num_max_right = str(right[Right_Index]) + num_max_right
                Right_Index += 1
            else:
                if num_to_left:
                    num_max_left = str(left[Left_Index]) + num_max_left
                else:
                    num_max_right = str(left[Left_Index]) + num_max_right
                Left_Index += 1

            num_to_left = not num_to_left  # Distribute the numbers on each of the list

        # Exhausting remaining index
        while Left_Index < len(left):   # left index is not exhausted
            if num_to_left:
                num_max_left = str(left[Left_Index]) + num_max_left
            else:
                num_max_right = str(left[Left_Index]) + num_max_right

            Left_Index += 1
            num_to_left = not num_to_left

        while Right_Index < len(right):  # right index is not exhausted
            if num_to_left:
                num_max_left = str(right[Right_Index]) + num_max_left
            else:
                num_max_right = str(right[Right_Index]) + num_max_right

            Right_Index += 1
            num_to_left = not num_to_left

        return [int(num_max_left), int(num_max_right)]

    else:  # Normal merging case
        while Left_Index < len(left) and Right_Index < len(right):
            if left[Left_Index] > right[Right_Index]:
                Merged.append(right[Right_Index])
                Right_Index += 1
            else:
                Merged.append(left[Left_Index])
                Left_Index += 1

        Merged += left[Left_Index:]
        Merged += right[Right_Index:]

        return Merged


def test_function(test_case):
    output = Rearrange_Digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


print('\nTest 1:')
list_num = [1, 2, 3, 4, 5]
result = Rearrange_Digits(input_list=list_num, first_layer=True)
print('Pass' if ([531, 42] == result) else 'Fail')


print('\nTest 2:')
list_num = [4, 6, 2, 5, 9, 8]
result = Rearrange_Digits(input_list=list_num, first_layer=True)
print('Pass' if ([852, 964] == result) else 'Fail')


print('\nTest 3:')
list_num = [1, 2, 3]
result = Rearrange_Digits(input_list=list_num, first_layer=True)
print('Pass' if ([31, 2] == result) else 'Fail')

print('\nEdge Cases:')
print('Test 4:')
list_num = [1, 1, 1]
result = Rearrange_Digits(input_list=list_num, first_layer=True)
print('Pass' if ([11, 1] == result) else 'Fail')


print('\nTest 5:')
list_num = [1]
result = Rearrange_Digits(input_list=list_num, first_layer=True)
print('Pass' if ([1] == result) else 'Fail')

print('\nTest 6:')
list_num = []
result = Rearrange_Digits(input_list=list_num, first_layer=True)
if not result:
    print('Pass \n')
else:
    print("Fail \n")
