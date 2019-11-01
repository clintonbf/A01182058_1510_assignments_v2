import random


def number_generator():
    """
    Generate a 6 random numbers between 1 - 49.
    List them in ascending order.

    :postcondition: a sequence of sorted numbers printed to stdout.
    """

    num_list = sorted(random.sample(range(49), 6))

    print(num_list)


def main():

    number_generator()


if __name__ == "__main__":
    main()

"""
Components of computational thinking  (decomposition, pattern matching, abstraction, algorithms) used in this script:
Abstraction is used here, via calls to range(), random(), and sorted().
"""