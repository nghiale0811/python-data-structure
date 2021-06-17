from typing import Optional, Any


class BSTNode:
    """A node class to represent a node in a BST.
    === Public Attributes ===
    item: Any The item stored in this node.
    left: Optional[BSTNode] The left child, or None if the node does not have a left child.
    right: Optional[BSTNode] The right child, or None if the node does not have a right child.
    """
    def __init__(self, item: Any, left: Optional['BSTNode'] = None,
                 right: Optional['BSTNode'] = None) -> None:
        """Initialize this node to store item and have children left
        and right."""
        self.item, self.left, self.right = item, left, right


def mirror(node: BSTNode) -> None:
    """
    Reverse a binary tree
    >>> n = BSTNode(4, BSTNode(2), BSTNode(5, None, BSTNode(6)))
    >>> mirror(n)
    >>> n.left.item
    5
    >>> n.right.item
    2
    >>> n.left.left.item
    6
    """
    tmp = node.right
    node.right = node.left
    node.left = tmp
    if node.right is not None:
        mirror(node.right)
    if node.left is not None:
        mirror(node.left)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
