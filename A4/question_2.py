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
    >>>gcd(192, 270)
    6
    """

    big_number = a
    small_number = b

    if b > a:
        big_number = b
        small_number = a

    try:
        remainder = big_number % small_number
    except TypeError:
        raise TypeError("Variables, a and b, must be integers")
    except ZeroDivisionError:
        raise ValueError("Variables, a and b, must be non-zero")
    else:
        while remainder != 0:
            big_number = small_number
            small_number = remainder
            remainder = big_number % small_number

        return small_number
