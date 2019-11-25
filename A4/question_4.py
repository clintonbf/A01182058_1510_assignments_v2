def is_this_element_the_smallest(lst: list, element) -> bool:
    """
    Determine if an element is the smallest in a list.

    :param element: int or string, an element in lst
    :param lst: a list
    :precondition: num is in lst
    :precondition: lst contains only integers OR strings
    :postcondition: determine if element is the smallest in lst
    :return: boolean

    >>> is_this_element_the_smallest([1, 2, 3, 4, 5], 1)
    True
    >>> is_this_element_the_smallest([16, 25, -3, 4, 5], 5)
    False
    >>> is_this_element_the_smallest([41, 2, 67, 1, 1], 1)
    True
    >>> is_this_element_the_smallest(['banana', 'a', 'pear', 'orange'], 'a')
    True
    """

    for item in lst:
        if element > item:
            return False

    return True


def find_smallest_elements_index(lst: list, start_index: int) -> int:
    """
    Find the list index of the smallest item in a list.

    :param lst: list
    :param start_index: integer
    :precondition: lst contains only integers OR strings
    :precondition: list is non_empty
    :precondition: start_index is in bounds of lst
    :postcondition: the index of the smallest element in lst is determined
    :return: int

    >>> find_smallest_elements_index([15, 23, -4, 1], 0)
    2
    >>> find_smallest_elements_index([-18, 23, -4, 1], 0)
    2
    >>> find_smallest_elements_index([0, 1, 2, 3], 0)
    2
    >>> find_smallest_elements_index([-6, 18, 9, 12, 32, -5, 121, 56], 1)
    5
    >>> find_smallest_elements_index(['crumble', 'pie', 'apple', 'strudel'], 0)
    2
    """

    sublist = lst[start_index:]

    for idx in range(0, len(sublist)):
        if is_this_element_the_smallest(sublist, sublist[idx]):
            return idx + start_index


def selection_sort(lst: list) -> list:
    """
    Sort a list.

    :param lst: list of strings or integers
    :precondition: all elements of lst are either strings or integers
    :precondition: lst is sortable
    :postcondition: lst is sorted
    :return: list

    >>> selection_sort([3, 5, 1, 9, -4])
    [-4, 1, 3, 5, 9]
    >>> selection_sort(['b', 'x', 'r', 'e', 'a'])
    ['a', 'b', 'e', 'r', 'x']
    >>> selection_sort(['apple', 'berry', 'e', 'cherry', 'hardware', 'aardvark'])
    ['aardvark', apple', 'berry', 'e', 'cherry', hardware]
    """

    try:
        for min_index in range(0, len(lst)):
            smallest_index = find_smallest_elements_index(lst, min_index)
            lst[min_index], lst[smallest_index] = lst[smallest_index], lst[min_index]
    except IndexError:
        raise IndexError("Variable, lst, is empty")
    except TypeError:
        raise TypeError("Variable, lst, must be a list. Contents must be sortable.")
    else:
        return lst[:]
