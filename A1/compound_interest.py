import doctest


def compound_interest(principal, interest, compound_freq, deposit_length):
    """
    Calculate savings growth at maturity.

    :param principal: float
    :param interest: float
    :param compound_freq: int
    :param deposit_length: int
    :precondition: principal must be a float
    :precondition: interest must be a float
    :precondition: compound_freq must be an int
    :precondition: deposit_length
    :postcondition: the amount of the investment upon maturity
    :return: float

    >>> compound_interest(100.1, 5.1, 4, 2)
    71826.59609112046
    """
    a = principal * (1 + interest/compound_freq) ** (compound_freq * deposit_length)

    return a


def main():
    # print("Test 1")
    # print(compound_interest(100.1, 5.1, 4, 2))
    # print("Test 2")
    # print(compound_interest(23, 2, 2, 50))
    # print("Test 3")
    # print(compound_interest(2.5, 56, 12, 12))

    doctest.testmod()


if __name__ == "__main__":
    main()

"""
Components of computational thinking  (decomposition, pattern matching, abstraction, algorithms) used in this script:
None were really used here. 
Abstraction could be argued to be used, since the actual calculation is done in a function rather than main()
"""