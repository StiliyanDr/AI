from collections import deque
from contextlib import contextmanager

from eightpuzzle import utility
from eightpuzzle.action import Action
from eightpuzzle.astar.frontier import Frontier
from eightpuzzle.astar.node import Node


class AStarSearch:
    """
    A callable representing the A* search algorithm for the 8-puzzle
    problem.
    """
    def __call__(self, initial_state, goal):
        """
        :param initial_state: A State instance representing the tiles' initial
        state.
        :param goal: A State instance representing the goal state.
        :returns: Returns a list of two-tuples with Action and State instances.
        The first tuple contains None and the initial state and each successive
        tuple contains an action applied to the state in the previous tuple and
        the state that results from it. If there is no solution, None is
        returned instead.
        """
        with self.__initialise_search(initial_state, goal):
            while not self.__frontier.is_empty:
                node = self.__frontier.extract_node_with_lowest_estimate()

                if (node.state != goal):
                    self.__explored.add(node.state)
                    self.__expand(node)
                else:
                    return self.__class__.__extract_solution_from(node)

            return None

    @contextmanager
    def __initialise_search(self, initial_state, goal):
        self.__frontier = Frontier(Node(initial_state))
        self.__explored = set()
        self.__goal = goal

        try:
            yield
        finally:
            self.__frontier = None
            self.__explored = None
            self.__goal = None

    def __expand(self, node):
        for action in Action:
            s = self.__make_successor_of(node, action)

            if (s is not None and s.state not in self.__explored):
                self.__frontier.add_or_update_if_estimate_is_less(s)

    def __make_successor_of(self, parent, action):
        successor = parent.state.after(action)

        return (
            Node(
                state=successor,
                estimate=self.__estimate_for(successor, parent),
                parent=parent,
                action=action
            )
            if (successor is not None)
            else None
        )

    def __estimate_for(self, state, parent):
        return (parent.estimate +
                1 +
                self.__number_of_misplaced_tiles_in(state))

    def __number_of_misplaced_tiles_in(self, state):
        return utility.number_of_differing_values_in(
            state.tiles,
            self.__goal.tiles
        )

    @staticmethod
    def __extract_solution_from(node):
        result = deque()

        while node is not None:
            result.appendleft((node.action, node.state))
            node = node.parent

        return list(result)
