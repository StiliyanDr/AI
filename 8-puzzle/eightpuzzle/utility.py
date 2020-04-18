
def contains_duplicates(items):
    """
    :param items: An iterable collection of hashable items.
    :returns: Returns a boolean value - whether the collection contains
    dulpicates.
    """
    return len(set(items) != len(items))


def identity(x):
    """
    The identity function.
    """
    return x


def empty_list_if_None(x):
    """
    Returns the argument itself, if it is not None and an empty list
    otherwise.
    """
    return (x
            if (x is not None)
            else [])


def values_of(list):
    """
    :param list: A list of lists.
    :returns: Returns a generator (iterator) which yields the list's
    values in row-first order.
    """
    for row in list:
        for value in row:
            yield value


def index_of(value, list, columns_count):
    """
    :param value: A value.
    :param list: A list of lists of equal length.
    :param columns_count: The number of columns per list.

    :returns: Returns a two-tuple of the row and column indexes,
    respectively, of the first occurrence of value in list. The search
    is done row-first.
    """
    for i, v in enumerate(values_of(list)):
        if (v == value):
            return divmod(i, columns_count)

    return None


def number_of_differing_values_in(lhs, rhs):
    """
    Takes two 2D lists which are assumed to have the same shape and
    returns the number of differing corresponding values in the lists.
    """
    corresponding_values = zip(values_of(lhs),
                               values_of(rhs))
    ones_for_differing_values = (
        1
        for a, b in corresponding_values
        if (a != b)
    )

    return sum(ones_for_differing_values)


def swap_values_at(first_position, second_position, list):
    """
    Swaps two values in-place in a list of lists.

    :param first_position: A two-tuple of integers - the index of the
    first value.
    :param second_position: A two-tuple of integers - the index of the
    second value.
    :param list: A list of lists.
    """
    i, j = first_position
    k, l = second_position

    list[i][j], list[k][l] = list[k][l], list[i][j]
