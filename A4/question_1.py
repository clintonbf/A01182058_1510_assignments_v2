import math


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

    >>>eratosthenes(30)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    >>>eratosthenes(0)
    []
    """

    # Main idea: populate a list to eliminate from since changing list size while iterating through it is bad

    try:
        no_multiples_beyond = int(math.sqrt(upperbound))
    except ValueError:
        raise ValueError("Variable, upperbound, must be greater than or equal to 0")
    else:
        # Populate it with all even numbers (other than 2)
        elimination_list = [num for num in range(4, (upperbound + 1), 2)]

        # Examine odd numbers
        for num in range(3, (no_multiples_beyond + 1), 2):
            elimination_list.extend(generate_multiples(num, upperbound))

        # Build the final list, excluding any number in elimination_list
        prime_list = [num for num in range(2, (upperbound + 1)) if num not in elimination_list]

        return prime_list
