import doctest


def confirm_colour(colour):
    """
    Confirm colour is valid.

    :param colour: string
    :precondition: string
    :postcondition: will verify if argument is a valid primary colour (red, blue, or yellow)
    :return: Boolean

    >>> confirm_colour("red")
    True
    >>> confirm_colour("BLUE")
    True
    >>> confirm_colour("Orange")
    False
    """

    colour = colour.lower()

    if colour == "red":
        is_valid = True
    elif colour == "blue":
        is_valid = True
    elif colour == "yellow":
        is_valid = True
    else:
        is_valid = False

    return is_valid


def output_error(colour):
    """
        Notify user that supplied colour is invalid.
    """
    print("Error. Your chosen colour, '" + colour + "', is invalid")
    print("Valid colours are 'red' or 'yellow' or 'blue'")


def assign_number_to_colour(colour):
    """
    Assign numerical value to a colour.

    :param colour: string
    :precondition: argument is "yellow", "blue" or "red"
    :postcondition: will assign a numerical value to the argument
    :return: int

    >>> assign_number_to_colour("blue")
    2
    """
    return_value = ""

    if colour == "red":
        return_value = 1
    elif colour == "blue":
        return_value = 2
    elif colour == "yellow":
        return_value = 3

    return return_value


def perform_colour_mix(colour_1, colour_2):
    """
    Get result of mixing two primary colours.

    :param colour_1: string
    :param colour_2: string
    :precondition: colour_1 is "yellow", "blue", or "red"
    :precondition: colour_2 is "yellow", "blue", or "red"
    :postcondition: the result of mixing the two colours is provided
    :return: string

    >>> perform_colour_mix("yellow", "blue")
    'green'
    """

    # By assigning numbers, I only have to test each combination 1 instead of twice
    colour_sum = assign_number_to_colour(colour_1) + assign_number_to_colour(colour_2)
    return_colour = ""

    if colour_sum == 3:
        return_colour = "purple"
    elif colour_sum == 4:
        return_colour = "orange"
    elif colour_sum == 5:
        return_colour = "green"

    return return_colour


def colour_mixer():
    """
    Mix two colours together.
    """
    first_colour = input("Enter your first primary colour (red, yellow, or blue): ")

    if confirm_colour(first_colour):
        if first_colour == "red":
            option_1 = "blue"
            option_2 = "yellow"
        elif first_colour == "blue":
            option_1 = "yellow"
            option_2 = "red"
        else:
            option_1 = "blue"
            option_2 = "red"

        second_colour = input("Enter your second primary colour (" + option_1 + " or " + option_2 + "): ")

        # Error check second colour
        if confirm_colour(second_colour):
            if first_colour == second_colour:
                print("Error: you may not enter a colour twice.")
                print("You entered '" + first_colour + "' & '" + second_colour + "'")
            else:  # Everything checks out, so combine the colours
                print("Secondary colour is '" + second_colour + "'")
                perform_colour_mix(first_colour, second_colour)
        else:
            output_error(second_colour)
    else:
        output_error(first_colour)


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()

"""Components of computational thinking  (decomposition, pattern matching, abstraction, algorithms) used in this script:
Decomposition was used to split out logic elements of combining two colours, converting colour names to numbers and
    printing out error messages.
Abstraction is employed when checking colours, and when producing the secondary colour.
An algorithm is used to error check both colours and halt if the first colour is invalid.
Pattern matching: not occurring   
"""
