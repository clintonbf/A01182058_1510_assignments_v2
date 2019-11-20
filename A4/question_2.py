def gcd(a: int, b: int) -> int:
    """
    Determine the greatest common divisor (GCD).

    :param a: integer
    :param b: integer
    :precondition: a & b != 0
    :precondition: a & b are integers
    :postcondition: the GCD of a & b is calculated
    :return: int

    >>>gcd(270, 192)
    6
    """

    # TODO: raise an exception if a or b is not a non-zero integer (or raise unless a & b are non-zero integers)

    big_number = a
    small_number = b

    if b > a:
        big_number = b
        small_number = a

    if small_number == 0:
        return 0

    remainder = big_number % small_number

    while remainder != 0:
        big_number = small_number
        small_number = remainder
        remainder = big_number % small_number

    return small_number


