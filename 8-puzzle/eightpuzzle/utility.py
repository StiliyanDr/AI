
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


def to_table(list, row_size=2):
    """
    Cuts a list into lists to form a table.

    :param list: A list.
    :param row_size: The row size of the resulting table.
    :returns: Cuts the list into lists with size row_size and forms a 2D
    list. If the row size does not divide the original list's length, the
    last row is shorter than the rest.
    """
    length = len(list)
    length_of_last_row = (row_size
                          if (divides(row_size, length))
                          else length % row_size)
    start_of_last_row = length - length_of_last_row

    return [
        list[start : start + row_size]
        for start in range(0, start_of_last_row + 1, row_size)
    ]


def divides(a, b):
    """
    :param a: A nonzero integer.
    :param b: An integer.
    :returns: Returns a boolean value indicating whether a divides b.
    """
    return b % a == 0
