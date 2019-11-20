def dijkstra(lst: list):
    """
    Sort a list of strings.

    :param lst: list of strings ['red', 'white', 'blue'] in any order, repeated any amount of times
    :precondition: lst is non-empty
    :precondition: lst can contain only ['red', 'white', 'blue']
    :postcondition: sorts list such that every 'red' appears first, then every 'white', then every 'blue'

    >>>dijkstra(['red', 'white', 'blue'])
    ['red', 'white', 'blue']
    >>>dijkstra(['blue', 'red', 'white', 'blue']
    ['red', 'white', 'blue', 'blue]
    >>>dijkstra(['white', 'blue', 'blue', 'red', 'white', 'red', 'white'])
    ['red', 'red', 'white', 'white', 'white', 'blue', 'blue']
    """

    lst.sort()

    # Find the last occurrence of 'blue'
    last_blue = 0
    for colour in lst:
        if colour == 'red':
            break
        else:
            last_blue += 1

    guard = 0
    while lst[guard] != 'red':
        del (lst[guard])
        lst.extend('blue')
        guard += 1

    # # Remove all instances of blue
    # for i in range(0, last_blue):
    #     del (lst[i])
    #
    # # Re-add all instances of blue
    # for i in range(0, last_blue):
    #     lst.extend('blue')
