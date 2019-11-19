import math


def eliminate_multiples(lst: list, divisor: int) -> list:
    """
    Generate a list of numbers that are not multiples of divisor.

    :param divisor: int
    :param lst: list
    :precondition: lst is non-empty
    :precondition: list contains only integers
    :precondition: divisor > 0
    :precondition: the sublist of lst that are not divisible by divisor is created
    :return: list

    >>> eliminate_multiples([0, 2, 3, 4, 5, 6], 2)
    [3, 5]
    """

    return [num for num in lst if num % divisor != 0]


def generate_multiples(divisor: int, upperbound: int) -> list:
    """
    Generate a list of multiples of a number.

    :param divisor: int, the base number to check against
    :param upperbound: int, the highest number to check against
    :precondition: upperbound > divisor
    :precondition: divisor > 0
    :precondition: divisor is an int
    :precondition: upperbound is an int
    :postcondition: a list of all numbers between divisor and upperbound that are divisible by divisor is generated
    :return:list

    >>> generate_multiples(2, 10)
    [4, 6, 8, 10]
    """
    return [num for num in range(divisor * 2, (upperbound + 1), divisor) if num % divisor == 0]


def eratosthenes(upperbound: int) -> list:
    """
    Determine all prime numbers in a range.

    :param upperbound: int
    :precondition: upperbound is an int
    :precondition: upperbound > 0
    :postcondition: all prime numbers between 0 and upper-bound are determined

    :return: list
    """
    # ToDo: Raise an exception if upperbound < 0

    # Take the square root of upper bound; check from 2 to that upperbound (0 & 1 are not prime)
    # Populate a list to eliminate from. I like this idea because I don't want to iterate through a list and eliminate

    prime_list = [2]
    upper_check_limit = int(math.sqrt(upperbound))

    # Populate it with all even numbers (other than 2)
    elimination_list = [num for num in range(4, (upper_check_limit + 1), 2)]

    # Range to examine is  [3, upper_check_limit] because all even numbers > 2 are divisible by 2 and thus aren't prime
    suspect_list = range(3, (upper_check_limit + 1), 2)

    for num in suspect_list:
        if num not in elimination_list:
            elimination_list.extend(generate_multiples(num, upper_check_limit))

    # Build the final list, excluding any number in elimination_list
    return [num for num in range(2, (upper_check_limit + 1)) if num not in elimination_list]


    # for i in range(3, (upper_check_limit + 1), 2):  # Save this cleverness for later





