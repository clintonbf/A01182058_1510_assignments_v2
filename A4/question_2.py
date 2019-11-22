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
    >>>gcd(270, 0)
    0
    """

    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a and b must be integers")

    if a == 0 or b == 0:
        raise ValueError("a and b must be non-zero")

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


