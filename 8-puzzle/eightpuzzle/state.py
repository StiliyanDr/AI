from copy import deepcopy as deep_copy_of
import csv

from eightpuzzle import utility
from eightpuzzle.action import Action


class State:
    """
    Represents a state of the 8-puzzle - a particular configuration of
    the tiles.
    """
    __DIMENSION = 3

    __BLANK_TILE = " "

    __TARGET_VALUES = frozenset(
        [__BLANK_TILE]
        +
        [str(i) for i in range(1, __DIMENSION ** 2)]
    )

    __TILES_DELIMITER = "|"

    @classmethod
    def from_CSV(cls, path):
        """
        Creates an instance from the contents of a CSV file.

        :param path: A string - the path of the CSV file.

        :raises FileNotFoundError: Raises an exception if the file does not
        exist.
        :raises ValueError: Raises an exception if the file's contents are
        not in the required format (see the constructor).
        """
        with open(path) as file:
            return cls(list(csv.reader(file)))

    def __init__(self, tiles):
        """
        :param tiles: A list of lists of strings whose shape is DIMENSION^2
        and whose values are TARGET_VALUES, in unspecified order.

        :raises ValueError: Raises an exception if tiles is not in the
        required format.
        """
        self.__set_tiles(tiles)
        self.__set_position_of_blank_tile()

    def __set_tiles(self, tiles):
        self.__class__.__validate(tiles)
        self.__tiles = tiles

    @classmethod
    def __validate(cls, tiles):
        cls.__validate_shape_of(tiles)
        cls.__validate_values_of(tiles)

    @classmethod
    def __validate_shape_of(cls, tiles):
        d = cls.__DIMENSION

        if (not (len(tiles) == d and
                 all(len(row) == d
                     for row in tiles))):
            raise ValueError(
                f"Shape must be {d}x{d}!"
            )

    @classmethod
    def __validate_values_of(cls, tiles):
        target_values = cls.__TARGET_VALUES

        if (set(utility.values_of(tiles)) != target_values):
            raise ValueError(
                f"Tiles' values must be {target_values}!"
            )

    def __set_position_of_blank_tile(self):
        self.__position_of_blank_tile = utility.index_of(
            self.__class__.__BLANK_TILE,
            self.__tiles,
            columns_count=self.__class__.__DIMENSION
        )

    def after(self, action):
        """
        :param action: An instance of Action.
        :returns: Returns a State instance - the state resulting from the
        passed action, or None if the action is invalid.
        """
        position = self.__blank_tile_position_after(action)

        return (State(self.__tiles_with_blank_moved_to(position))
                if (position is not None)
                else None)

    def __blank_tile_position_after(self, action):
        i, j = self.__position_of_blank_tile

        new_position = (
            (i, j - 1)
            if (action is Action.LEFT)
            else (i, j + 1)
            if (action is Action.RIGHT)
            else (i - 1, j)
            if (action is Action.UP)
            else (i + 1, j)
        )

        return (new_position
                if (self.__class__.__is_valid_position(new_position))
                else None)

    @classmethod
    def __is_valid_position(cls, position):
        return all(0 <= i < cls.__DIMENSION
                   for i in position)

    def __tiles_with_blank_moved_to(self, position):
        assert self.__class__.__is_valid_position(position)

        new_tiles = self.tiles
        utility.swap_values_at(
            position,
            self.__position_of_blank_tile,
            new_tiles
        )

        return new_tiles

    @property
    def tiles(self):
        """
        :returns: Returns a two-dimensional list (a list of lists) that
        represents the tiles.
        """
        return deep_copy_of(self.__tiles)

    def __eq__(self, rhs):
        """
        :param rhs: A value.
        :returns: Returns a boolean value indicating whether rhs is a State
        instance representing the same arrangement of the tiles.
        """
        return (isinstance(rhs, self.__class__) and
                self.__tiles == rhs.__tiles)

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        d = self.__class__.__TILES_DELIMITER
        rows = (d.join(row) for row in self.__tiles)

        return "\n".join(rows)

    def __repr__(self):
        return (f"{self.__class__.__name__}("
                f"{self.__tiles!r})")
