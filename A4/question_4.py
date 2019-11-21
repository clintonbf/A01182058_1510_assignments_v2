def find_smallest_number_element(lst: list) -> int:
    """
    Find the element of the smallest number in a list.

    :param lst: list
    :precondition: lst is non-empty
    :precondition: lst values are all integers
    :postcondition: the element of the smallest number in the list is determined
    :postcondition: where a value is repeated, the smaller of the two elements is the output
    :return: int

    >>> find_smallest_number_element([15, 23, -4, 1])
    2
    >>> find_smallest_number_element([0, 1, 2, 3])
    0
    >>> find_smallest_number_element([49, 18, 9, 12, 32, 9, 121, 56])
    2
    """

    sorted_list = sorted(lst)

    smallest_index = 0
    if sorted_list[0] == lst[0]:
        return 0
    else:
        while lst[smallest_index] != sorted_list[0]:
            smallest_index += 1

    return smallest_index


def selection_sort(lst: list) -> list:
    """
    Sort a list.

    :param lst: list of integers
    :precondition: all elements of lst are integers
    :postcondition: lst is sorted
    :return: list
    """

    element_order = []

    # for i in range(0, len(lst)):
    #     element_order.append(find_smallest_number_element(lst[i:]))

    element_order = [find_smallest_number_element(lst[i:]) for i in range(0, len(lst))]

    return [lst[element] for element in element_order]
