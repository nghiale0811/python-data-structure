from typing import Any, List, Optional


class Queue:
    """A first-in-first-out (FIFO) queue of items.

    Stores data in a first-in, first-out order. When removing an item from the
    queue, the most recently-added item is the one that is removed.
    """
    _items: List

    def __init__(self) -> None:
        """Initialize a new empty queue."""
        self._items = []

    def is_empty(self) -> bool:
        """Return whether this queue contains no items.

        >>> q = Queue()
        >>> q.is_empty()
        True
        >>> q.enqueue('hello')
        >>> q.is_empty()
        False
        """
        return self._items == []

    def enqueue(self, item: Any) -> None:
        """Add <item> to the back of this queue.
        """
        self._items.append(item)

    def dequeue(self) -> Optional[Any]:
        """Remove and return the item at the front of this queue.

        Return None if this Queue is empty.
        (We illustrate a different mechanism for handling an erroneous case.)

        >>> q = Queue()
        >>> q.enqueue('hello')
        >>> q.enqueue('goodbye')
        >>> q.dequeue()
        'hello'
        """
        return self._items.pop(0)

    def reverse_and_remove_odds(self) -> None:
        """
        Reverse the order of items in the queue and remove odd numbers
        """
        self._reverse_and_remove_odds_helper(self.dequeue())
        return

    def _reverse_and_remove_odds_helper(self, item) -> None:

        if self.is_empty():
            return
        self._reverse_and_remove_odds_helper(self.dequeue())
        if item % 2 == 0:
            self.enqueue(item)
        return
