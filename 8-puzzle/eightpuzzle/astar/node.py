
class Node:
    """
    Represents a node for a search. Has the following read-only
    attributes:
     - state: the state to which the node corresponds
     - estimate: the estimated path cost of a solution through this
       node
     - parent: the parent node
     - action: the action that lead to the generation of the node's
       state.
    """
    def __init__(self,
                 state,
                 estimate=0,
                 parent=None,
                 action=None):
        """
        :param state: A State instance.
        :param estimate: A non-negative integer. Defaults to 0.
        :param parent: A Node instance. Defaults to None.
        :param action: An instance of Action. Defaults to None.
        """
        self.__state = state
        self.__estimate = estimate
        self.__parent = parent
        self.__action = action

    @property
    def state(self):
        return self.__state

    @property
    def estimate(self):
        return self.__estimate

    @property
    def parent(self):
        return self.__parent

    @property
    def action(self):
        return self.__action

    def __eq__(self, rhs):
        """
        :param rhs: A value.
        :returns: Returns a boolean value indicating whether rhs is a Node
        instance corresponding to the same state.
        """
        return (isinstance(rhs, self.__class__) and
                self.state == rhs.state)

    def __hash__(self):
        return hash(self.state)
