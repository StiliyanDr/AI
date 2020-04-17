"""
A wrapper of the standard 'heapq' module.

All names imported from it as public names are part of the API.
"""


from heapq import (
    heapify,
    heappop as extract_min_from,
    heappush as insert_in,
)


def update_item_in(heap, index, new_item):
    """
    Replaces an item in a binary heap with one which is less than or
    equal to it.

    :param heap: A list representing a binary heap.
    :param index: A position within the heap representation indicating
    the item to update.
    :param new_item: An item not greater than the one to be replaced. 
    """
    _verify_new_item_is_not_greater(new_item,
                                    heap,
                                    index)

    heap[index] = new_item
    _sift_up_item_at(index, heap)


def _verify_new_item_is_not_greater(item, heap, index):
    if (heap[index] < item):
        raise ValueError(
            "New item can't be greater than the old one!"
        )


def _sift_up_item_at(index, heap):
    item = heap[index]

    while (not _is_root(index)):
        p = _parent_of(index)

        if (item < heap[p]):
            heap[index] = heap[p]
            index = p
        else:
            break

    heap[index] = item


def _is_root(index):
    return index == 0


def _parent_of(index):
    assert index > 0

    return (index - 1) // 2
