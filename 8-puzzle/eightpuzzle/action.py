import enum


@enum.unique
class Action(enum.Enum):
    """
    Represents an action in the 8-puzzle problem, that is, a direction
    for a movement of the blank tile.
    """
    LEFT = enum.auto()
    RIGHT = enum.auto()
    UP = enum.auto()
    DOWN = enum.auto()
