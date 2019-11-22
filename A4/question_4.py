def is_this_number_smallest(lst: list, num: int) -> bool:
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


def find_smallest_number_element(lst: list, start_index: int) -> int:
    """
    Find the array element of the smallest number in a list.

    :param lst: list
    :param start_index: integer
    :precondition: lst contains only integers
    :precondition: list is non_empty
    :precondition: start_index is in bounds of lst
    :postcondition: the index of the smallest element in lst is determined
    :return: int

    >>> find_smallest_number_element([15, 23, -4, 1], 0)
    2
    >>> find_smallest_number_element([-18, 23, -4, 1], 0)
    2
    >>> find_smallest_number_element([0, 1, 2, 3], 0)
    2
    >>> find_smallest_number_element([-6, 18, 9, 12, 32, -5, 121, 56], 1)
    5
    """

    sublist = lst[start_index:]

    for idx in range(0, len(sublist)):
        if is_this_number_smallest(sublist, sublist[idx]):
            return idx + start_index


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

    :param lst: list of strings or integers
    :precondition: all elements of lst are either strings or integers
    :postcondition: lst is sorted
    :return: list

    >>> selection_sort([3, 5, 1, 9, -4])
    [-4, 1, 3, 5, 9]
    >>> selection_sort(['b', 'x', 'r', 'e', 'a'])
    ['a', 'b', 'e', 'r', 'x']
    >>> selection_sort(['apple', 'berry', 'e', 'cherry', 'hardware', 'aardvark'])
    ['aardvark', apple', 'berry', 'e', 'cherry', hardware]
    """

    if not isinstance(lst, list):
        raise TypeError("lst must be a list")

    for item in lst:
        if not isinstance(item, int) and not isinstance(item, str):
            raise TypeError("list items must be either all integers or strings.", item, "is not a string.")

    for min_index in range(0, len(lst)):
        smallest_index = find_smallest_number_element(lst, min_index)
        swap_elements(lst, smallest_index, min_index)

    return lst[:]
