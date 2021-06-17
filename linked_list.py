"""Lab 5: Linked List Exercises

=== CSC148 Fall 2020 ===
Department of Mathematical and Computational Sciences,
University of Toronto Mississauga

=== Module Description ===
This module contains the code for a linked list implementation with two classes,
LinkedList and _Node.

All of the code from lecture is here, as well as some exercises to work on.
"""
from __future__ import annotations
from typing import Any, List, Optional


class _Node:
    """A node in a linked list.

    Note that this is considered a "private class", one which is only meant
    to be used in this module by the LinkedList class, but not by client code.

    === Attributes ===
    item:
        The data stored in this node.
    next:
        The next node in the list, or None if there are no more nodes.
    """
    item: Any
    next: Optional[_Node]

    def __init__(self, item: Any) -> None:
        """Initialize a new node storing <item>, with no next node.
        """
        self.item = item
        self.next = None  # Initially pointing to nothing


class LinkedList:
    """A linked list implementation of the List ADT.
    """
    # === Private Attributes ===
    # _first:
    #     The first node in the linked list, or None if the list is empty.
    _first: Optional[_Node]

    def __init__(self, items: list) -> None:
        """Initialize a new empty linked list containing the given items.
        """
        self._first = None
        self.items = items
        if items:
            self._first = _Node(items[0])
            curr = self._first
            i = 1
            while i < len(items):
                curr.next = _Node(items[i])
                curr = curr.next
                i += 1

    # ------------------------------------------------------------------------
    # Methods from lecture/readings
    # ------------------------------------------------------------------------
    def is_empty(self) -> bool:
        """Return whether this linked list is empty.

        # >>> LinkedList([]).is_empty()
        # True
        # >>> LinkedList([1, 2, 3]).is_empty()
        # False
        """
        return self._first is None

    def __str__(self) -> str:
        """Return a string representation of this list in the form
        '[item1 -> item2 -> ... -> item-n]'.

        # >>> str(LinkedList([1, 2, 3]))
        # '[1 -> 2 -> 3]'
        # >>> str(LinkedList([]))
        # '[]'
        """
        items = []
        curr = self._first
        while curr is not None:
            items.append(str(curr.item))
            curr = curr.next
        return '[' + ' -> '.join(items) + ']'

    def __getitem__(self, index: int) -> Any:
        """Return the item at position <index> in this list.

        Raise IndexError if <index> is >= the length of this list.
        """
        curr = self._first
        curr_index = 0

        while curr is not None and curr_index < index:
            curr = curr.next
            curr_index += 1

        assert curr is None or curr_index == index

        if curr is None:
            raise IndexError
        else:
            return curr.item

    def insert(self, index: int, item: Any) -> None:
        """Insert the given item at the given index in this list.

        Raise IndexError if index > len(self) or index < 0.
        Note that adding to the end of the list is okay.

        # >>> lst = LinkedList([1, 2, 10, 200])
        # >>> lst.insert(2, 300)
        # >>> str(lst)
        # '[1 -> 2 -> 300 -> 10 -> 200]'
        # >>> lst.insert(5, -1)
        # >>> str(lst)
        # '[1 -> 2 -> 300 -> 10 -> 200 -> -1]'
        # >>> lst.insert(100, 2)
        # Traceback (most recent call last):
        # IndexError
        """
        # Create new node containing the item
        new_node = _Node(item)

        if index == 0:
            self._first, new_node.next = new_node, self._first
        else:
            # Iterate to (index-1)-th node.
            curr = self._first
            curr_index = 0
            while curr is not None and curr_index < index - 1:
                curr = curr.next
                curr_index += 1

            if curr is None:
                raise IndexError
            else:
                # Update links to insert new node
                curr.next, new_node.next = new_node, curr.next

    # ------------------------------------------------------------------------
    # Lab Task 1
    # ------------------------------------------------------------------------
    # TODO: implement this method
    def __len__(self) -> int:
        """Return the number of elements in this list.

        # >>> lst = LinkedList([])
        # >>> len(lst)              # Equivalent to lst.__len__()
        # 0
        # >>> lst = LinkedList([1, 2, 3])
        # >>> len(lst)
        # 3
        """
        cnt = 0
        curr = self._first
        while curr is not None:
            curr = curr.next
            cnt += 1
        return cnt

    # TODO: implement this method
    def count(self, item: Any) -> int:
        """Return the number of times <item> occurs in this list.

        Use == to compare items.

        # >>> lst = LinkedList([1, 2, 1, 3, 2, 1])
        # >>> lst.count(1)
        # 3
        # >>> lst.count(2)
        # 2
        # >>> lst.count(3)
        # 1
        """
        cnt = 0
        curr = self._first
        while curr is not None:
            if item == curr.item:
                cnt += 1
            curr = curr.next
        return cnt

    # TODO: implement this method
    def index(self, item: Any) -> int:
        """Return the index of the first occurrence of <item> in this list.

        Raise ValueError if the <item> is not present.

        Use == to compare items.

        # >>> lst = LinkedList([1, 2, 1, 3, 2, 1])
        # >>> lst.index(1)
        # 0
        # >>> lst.index(3)
        # 3
        # >>> lst.index(148)
        # Traceback (most recent call last):
        # ValueError
        """
        cnt = 0
        curr = self._first
        if item == curr.item:
            return 0
        while curr is not None:
            cnt += 1
            if cnt == len(self):
                raise ValueError
            curr = curr.next
            if item == curr.item:
                break
        return cnt

    # TODO: implement this method
    def __setitem__(self, index: int, item: Any) -> None:
        """Store item at position <index> in this list.

        Raise IndexError if index >= len(self).

        # >>> lst = LinkedList([1, 2, 3])
        # >>> lst[0] = 100  # Equivalent to lst.__setitem__(0, 100)
        # >>> lst[1] = 200
        # >>> lst[2] = 300
        # >>> str(lst)
        # '[100 -> 200 -> 300]'
        """
        if index >= len(self.items):
            raise IndexError
        curr_index = 0
        curr = self._first
        if index == 0:
            curr.item = item
        else:
            while curr is not None and curr_index < index:
                curr = curr.next
                curr_index += 1
            curr.item = item

    def delete_node(self, id: int) -> int:
        """
        Precondition: k >= 1
        >>> lst = LinkedList([1, 2, 3])
        >>> lst.delete_node(1)
        2
        >>> lst._first.item
        1
        >>> lst._first.next.item
        2
        """
        curr = self._first
        if self.is_empty():
            return self._first.item
        elif id == 1:
            curr = curr.next
            item = curr.item
            node = curr.next.next
            curr.next = node
            return item
        curr.next = self.delete_node(id - 1)

    def keep_biggest(self, other: LinkedList):
        """
        >>> lst1 = LinkedList([2, 5, 10, 12, 0])
        >>> lst2 = LinkedList([1, 20, 10, 99])
        >>> str(lst1)
        '[2 -> 5 -> 10 -> 12 -> 0]'
        >>> lst1.keep_biggest(lst2)
        >>> str(lst1)
        '[2 -> 10 -> 0]'
        """
        curr1 = self._first
        curr2 = other._first
        if curr1.item < curr2.item:
            curr1 = curr1.next
        while curr1 is not None and curr2 is not None:
            if curr1.next.item < curr2.next.item and \
                    curr1.next.next is not None:
                tmp = curr1.next.next
                curr1.next = tmp
            elif curr1.next.item < curr2.next.item:
                curr1.item = curr1.next.item
                curr1.next = None
                break
            curr1 = curr1.next
            curr2 = curr2.next


if __name__ == '__main__':
    # import python_ta
    # python_ta.check_all()
    import doctest
    doctest.testmod()
