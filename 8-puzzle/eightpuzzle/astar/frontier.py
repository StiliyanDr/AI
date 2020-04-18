from eightpuzzle import priorityqueue


_PriorityQueue = priorityqueue.define_priority_queue_class(
    key_accessor=lambda node: node.estimate
)


class Frontier:
    """
    Represents the frontier of an A-star search.
    """
    def __init__(self, initial_node):
        """
        Initialises the frontier with a single node.
        """
        self.__nodes = _PriorityQueue([initial_node])

    def extract_node_with_lowest_estimate(self):
        """
        Extracts a node with with a lowest estimate from the frontier.
        """
        assert not self.is_empty

        return self.__nodes.extract_minimal()

    @property
    def is_empty(self):
        """
        Returns a boolean value indicating whether the frontier is empty.
        """
        return self.__nodes.is_empty

    def add_or_update_if_estimate_is_less(self, node):
        """
        Receives a node and inserts it into the frontier, if there is no node
        with the same corresponding state in the frontier. Otherwise replaces
        the node already in the frontier only if its estimate is greater.
        """
        if (node not in self):
            self.__nodes.add(node)
        else:
            self.__nodes.update_if_key_is_less(node)

    def __contains__(self, node):
        """
        :param node: A Node instance.
        :returns: Returns a boolean value indicating whether the frontier
        contains a node that has the same corresponding state.
        """
        return node in self.__nodes
