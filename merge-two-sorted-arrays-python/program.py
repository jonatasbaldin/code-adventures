# Merge Two Sorted Arrays Python
# https://www.youtube.com/watch?v=xF3TU-QlhJQ

# This method is O(n).

input_a = ([10], [2, 3])
output_a = [2, 3, 10]

input_b = ([3, 8, 9], [4, 7, 8])
output_b = [3, 4, 7, 8, 8, 9]


def merge_array(arr1, arr2):
    i = 0
    j = 0
    arr3 = []

    # First, traverse arr1 and arr2, while their size are bigger than the indexes used
    while (i < len(arr1) and j < len(arr2)):
        
        # If the element of arr1 is smaller than arr2, add to arr3 and increment the i index
        # In the second example, we will compare 5 and 3, since 3 is smaller than 5
        # we add 3 to arr3 and move the pointer from arr1 forward (since we used its element)
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i = i + 1
        # Otherwise, we just do the contrary, we add the element from arr2 into arr3
        # and move the pointer from arr2 forward (since we used its element)
        else:
            arr3.append(arr2[j])
            j = j + 1

    # One of the conditions from the while above will fail when the smallest array is exhausted
    # Then, we may have some elements hanging from one array that we need to copy and past to arr3
    # The two while loops below go through both arrays and copy the remaining elements
    # Since one of them was exhausted, just one loop will be executed

    while (i < len(arr1)):
        arr3.append(arr1[i])
        i = i + 1

    while (j < len(arr2)):
        arr3.append(arr2[j])
        j = j + 1

    print(f'Arr1: {arr1}')
    print(f'Arr2: {arr2}')
    print(f'Result: {arr3}')
    print('#' * 70)
    return arr3


def test_input_a():
    result = merge_array(input_a[0], input_a[1])
    assert result == output_a


def test_input_b():
    result = merge_array(input_b[0], input_b[1])
    assert result == output_b

test_input_a()
test_input_b()