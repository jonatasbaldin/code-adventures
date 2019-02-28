def binary_search(sorted_list, item):
    """
    Implements a Binary Search, O(log n).

    If item is is list, returns amount of steps.
    If item not in list, returns None.
    """

    steps = 0
    start = 0
    end = len(sorted_list)

    while start < end:
        steps += 1

        mid = (start + end) // 2
        # print("#", mid)

        if sorted_list[mid] == item:
            return steps

        # If the item is lesser than the list
        # item == 3 and sorted_list == [1, 2, 3, 4, 5, 6, 8]
        # the END of my list becomes the middle (4), excluding all items from the middle to the end
        # end == 4
        # next time, when mid = (start + end) // 2 executes, mid == 2
        if sorted_list[mid] > item:
            end = mid

        # If the item is bigger than the list
        # item == 8 and sorted_list == [1, 2, 3, 4, 5, 6, 8]
        # the START of my list will be the middle (4) plus 1, excluding all items from the middle to the begginning
        # start == 5
        # next time, when mid = (start + end) // 2 executes, mid == 8
        if sorted_list[mid] < item:
            start = mid + 1

    return None


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11))  # None
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8))  # 3
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8], 8))  # 3
print(binary_search(list(range(0, 240000)), 0))  # 18
print(binary_search(list(range(0, 240000)), 239999))  # 17

# 4 billion, can't run on my machine hah
# print(binary_search(list(range(0, 4000000000)), 0))  #  killed     python binary_search.py