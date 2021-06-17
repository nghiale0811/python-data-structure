from typing import List


class Tree:
    def __init__(self, item: object = None, parent: 'Tree' = None,
                 children: list = None):
        self.item = item
        self.parent = parent
        if not children:
            self.children = []
        else:
            self.children = children[:]


class LLNode:
    def __init__(self, item: object, next: 'LLNode' = None):
        self.item, self.next = item, next

    def __str__(self) -> str:
        return str(self.item) + (' -> ' + str(self.next) if self.next else '')


def path_from_root_as_list(t: Tree) -> list:
    if t.parent is None:
        return [t.item]
    else:
        return path_from_root_as_list(t.parent) + [t.item]


def path_from_root_as_linked_list(t: Tree) -> LLNode:
    if t.parent is None:
        return LLNode(t.item)
    else:
        path_from_root_as_linked_list(t.parent).next = LLNode(t.item)
