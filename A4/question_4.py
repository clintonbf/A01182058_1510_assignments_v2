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
    sorted_list = sorted(lst)

    smallest_index = min_index
    if sorted_list[0] == lst[0]:
        return 0
    else:
        while lst[smallest_index] != sorted_list[0]:
            smallest_index += 1

    return smallest_index


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
    """

    # TODO Raise error if lst is NOT a non-empty list of sortable items

    working_copy = lst[:]  # This will be a shallow copy, which may not be good enough...

    for min_index in range(0, len(working_copy)):
        smallest_index = find_smallest_number_element(working_copy, min_index)
        swap_elements(working_copy, smallest_index, min_index)

    return working_copy
