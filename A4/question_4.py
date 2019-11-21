def find_smallest_number_element(lst: list, min_index: int) -> int:
    """
    Find the element of the smallest number in a list.

    :param min_index: int, smallest index to start checking from
    :param lst: list
    :precondition: lst is non-empty
    :precondition: lst values are all integers
    :precondition: min_index < len(lst)
    :postcondition: the element of the smallest number in the list is determined
    :postcondition: where a value is repeated, the smaller of the two elements is the output
    :return: int

    >>> find_smallest_number_element([15, 23, -4, 1], 0)
    2
    >>> find_smallest_number_element([-18, 23, -4, 1], 0)
    2
    >>> find_smallest_number_element([0, 1, 2, 3], 0)
    2
    >>> find_smallest_number_element([49, 18, 9, 12, 32, 9, 121, 56], 0)
    2
    """

    # TODO: add additional DJE's wrt to min_index
    # TODO: using sorted to make this work is surely NOT valid
    sorted_list = sorted(lst)

    smallest_index = min_index
    if sorted_list[min_index] == lst[min_index]:  # is the first element in the sorted list the first element in lst?
        return min_index
    else:
        while lst[smallest_index] != sorted_list[0]:
            smallest_index += 1

    return smallest_index


def is_this_number_smallest(num: int, lst: list) -> bool:
    """
    Determine if a number is the smallest in a list.

    :param num: int, a number in lst
    :param lst: a list of integers
    :precondition: num is in lst
    :precondition: lst contains only integers
    :postcondition: determine if num is the smallest number in lst
    :return: boolean

    >>> is_this_number_smallest(1, [1, 2, 3, 4, 5])
    True
    >>> is_this_number_smallest(5, [16, 25, -3, 4, 5])
    False
    >>> is_this_number_smallest(1, [41, 2, 67, 1, 1])
    True
    """

    for number in lst:
        if num > number:
            return False

    return True


def find_smallest_number_element_2(lst: list, start_index: int) -> int:
    """
    Find the array element of the smallest number in a list.

    :param lst: list
    :param start_index: integer
    :precondition: lst contains only integers
    :precondition: list is non_empty
    :precondition: start_index is in bounds of lst
    :postcondition: the index of the smallest element in lst is determined
    :return: int

    >>> find_smallest_number_element_2([15, 23, -4, 1], 0)
    2
    >>> find_smallest_number_element_2([-18, 23, -4, 1], 0)
    2
    >>> find_smallest_number_element_2([0, 1, 2, 3], 0)
    2
    >>> find_smallest_number_element_2([-6, 18, 9, 12, 32, -5, 121, 56], 1)
    5
    """

    smallest_idx = 0

    for idx in range(start_index, (len(lst) - 1)):
        if is_this_number_smallest(lst[idx], lst):
            return idx


def swap_elements(lst: list, frm: int, to: int):
    """
    Swap two list elements.

    :param lst: list
    :param frm: int, the index of the element that you want to swap in lst
    :param to: int, the index of the element in lst where you want frm to move into
    :precondition: frm is an element in lst
    :precondition: to is an element in lst
    :postcondition: the values in to and frm switch positions in lst

    >>> swap_elements([1, 2, 3, 4], 1, 3)
    [1, 4, 3, 2]
    """

    frm_value = lst[frm]
    to_value = lst[to]

    lst[to] = frm_value
    lst[frm] = to_value


def selection_sort(lst: list) -> list:
    """
    Sort a list.

    :param lst: list of integers
    :precondition: all elements of lst are integers
    :postcondition: lst is sorted
    :return: list

    >>> selection_sort([3, 5, 1, 9, -4])
    [-4, 1, 3, 5, 9]
    """

    # TODO Raise error if lst is NOT a non-empty list of sortable items

    working_copy = lst[:]  # This will be a shallow copy, which may not be good enough...

    for min_index in range(0, len(working_copy)):
        smallest_index = find_smallest_number_element(working_copy, min_index)
        print("Found smallest index", smallest_index, "value =", working_copy[smallest_index])
        swap_elements(working_copy, smallest_index, min_index)

    return working_copy
