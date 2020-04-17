from copy import deepcopy as deep_copy_of
from operator import lt as less

from eightpuzzle import (
    binaryheap,
    utility,
)


class PriorityQueueError(Exception):
    """
    The base class for exceptions raised by the 'priorityqueue' module.
    """
    pass


def define_priority_queue_class(key_accessor=utility.identity,
                                comparator=less):
    """
    Defines a min priority queue class containing hashable "items"
    which have keys associated with them.

    :param key_accessor: A unary function taking an item and returning
    its associated key. This function is assumed to raise no
    exceptions. Defaults to the identity function.
    :param comparator: A function taking two keys and returning a
    boolean value - whether the first key is considered less than the
    second one. This function is assumed to raise no exceptions.
    Defaults to the < operator on items.
    """
    class PriorityQueue:
        """
        Implements the min priority queue ADT.
        """
        class __Element:
            """
            A non-public class representing elements of the priority queue.
            """
            def __init__(self, item):
                self.__item = item

            def __lt__(self, rhs):
                return comparator(self.key, rhs.key)

            @property
            def key(self):
                return key_accessor(self.__item)

            def __eq__(self, rhs):
                return self.item == rhs.item

            @property
            def item(self):
                return self.__item

        def __init__(self, items=None):
            """
            :param items: An iterable collection of unique items - the initial
            contents of the priority queue. If omitted, the queue will be
            empty.

            :raises PriorityQueueError: Raises an exception if the collection
            contains duplicates.
            """
            items = utility.empty_list_if_None(items)
            self.__set_unique_items(items)
            self.__build_heap_for(items)

        def __set_unique_items(self, items):
            self.__items = set(items)

            if (len(self.__items) != len(items)):
                raise PriorityQueueError(
                    "No duplicate items are allowed!"
                )

        def __build_heap_for(self, items):
            self.__elements = [self.__class__.__Element(i)
                               for i in items]
            binaryheap.heapify(self.__elements)

        def add(self, item):
            """
            Adds an item to the queue.

            :param item: An item which is not already in the queue.

            :raises PriorityQueueError: Raises an exception if the item is
            already present in the queue.
            """
            self.__verify_item_is_not_already_present(item)
            binaryheap.insert_in(self.__elements,
                                 self.__class__.__Element(item))
            self.__items.add(item)

        def __verify_item_is_not_already_present(self, item):
            if (item in self):
                raise PriorityQueueError(
                    "Item is already present in the queue!"
                )

        def __contains__(self, item):
            """
            :param item: An item.
            :returns: Returns a boolean value indicating whether the item is in
            the priority queue.
            """
            return item in self.__items

        @property
        def minimal(self):
            """
            :returns: Returns a deep copy an item with a minimal key.

            :raises PriorityQueueError: Raises an exception if the queue is
            empty.
            """
            self.__verify_queue_is_not_empty()

            return deep_copy_of(self.__elements[0].item)

        def __verify_queue_is_not_empty(self):
            if (self.is_empty):
                raise PriorityQueueError("The queue is empty!")

        @property
        def is_empty(self):
            """
            Returns a boolean value indicating whether the queue is empty.
            """
            return not bool(self.__items)

        def extract_minimal(self):
            """
            Removes and returns an item with a minimal key.

            :raises PriorityQueueError: Raises an exception if the queue is
            empty.
            """
            self.__verify_queue_is_not_empty()

            result = binaryheap.extract_min_from(self.__elements).item
            self.__items.remove(result)

            return result

        def update_if_key_is_less(self, item):
            """
            Updates an item in the queue if its new key is less than the one
            already present.

            :param item: The item to be potentially updated.

            :raises PriorityQueueError: Raises an exception if the item is not
            in the queue.
            """
            element = self.__class__.__Element(item)
            p = self.__position_of(element)

            if (element < self.__elements[p]):
                binaryheap.update_item_in(self.__elements,
                                          index=p,
                                          new_item=element)

        def __position_of(self, element):
            try:
                return self.__elements.index(element)
            except ValueError:
                raise PriorityQueueError(
                    "Item not in queue!"
                )

        def __iter__(self):
            """
            Returns a generator (iterator) which extracts a minimal element
            from the queue each time it is prompted for its next value (until
            the queue is empty).
            """
            while not self.is_empty:
                yield self.extract_minimal()

    return PriorityQueue
