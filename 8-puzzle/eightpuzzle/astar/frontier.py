from pqdict import minpq as MinPriorityQueue


class Frontier:
    """
    Represents the frontier of an A-star search.
    """
    def __init__(self, initial_node):
        """
        Initialises the frontier with a single node.
        """
        self.__nodes = MinPriorityQueue({initial_node : initial_node.estimate})

    def extract_node_with_lowest_estimate(self):
        """
        Extracts a node with with a lowest estimate from the frontier.
        """
        assert not self.is_empty
        node, _ = self.__nodes.popitem()

        return node

    @property
    def is_empty(self):
        """
        Returns a boolean value indicating whether the frontier is empty.
        """
        return len(self.__nodes) == 0

    def add_or_update_if_estimate_is_less(self, node):
        """
        Receives a node and inserts it into the frontier, if there is no node
        with the same corresponding state in the frontier. Otherwise replaces
        the node already in the frontier only if its estimate is greater.
        """
        estimate = node.estimate

        if (node not in self):
            self.__nodes.additem(node, estimate)
        elif (estimate < self.__nodes[node]):
            self.__nodes.updateitem(node, estimate)

    def __contains__(self, node):
        """
        :param node: A Node instance.
        :returns: Returns a boolean value indicating whether the frontier
        contains a node that has the same corresponding state.
        """
        return node in self.__nodes
