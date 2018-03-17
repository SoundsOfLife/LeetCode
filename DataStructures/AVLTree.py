class Node:
    def __init__(self, value):
        self.value = None
        self.left = None
        self.right = None
        self.height = None


def Height(node):
    if node is None:
        return -1
    else:
        return node.height


def Find(x, root):
    if root is None or root.value == x:
        return root
    elif root.value < x:
        if root.left is None:
            return None
        else:
            return Find(x, root.left)
    elif root.vlaue > x:
        if root.right is None:
            return None
        else:
            return Find(x, root.right)


def FindMin(root):
    if root is None:
        return None
    elif root.left is None:
        return root
    else:
        return FindMin(root.left)


def FindMax(root):
    if root is None:
        return None
    else:
        while root.right is not None:
            root = root.right
        return root


def SingleLeft(node):
    root = node.left
    node.left = root.right
    root.right = node.right
    root.height = max(Height(root.left), Height(root.right)) + 1
    node.height = max(Height(root.left), Height(root.right)) + 1
    return root


def SingleRight(node):
    root = node.right

    return root


def DoubleLeft(node):
    node.left = SingleRight(node.left)

    return SingleLeft(node)


def DoubleRight(node):
    node.right = SingleLeft(node.right)

    return SingleRight(node)


def Insert(x, root):
    if root is None:
        root = Node()
        root.value = x
        return root
    else:
        if root.value > x:
            root.left = Insert(x, root.left)
            if Height(root.left) - Height(root.right) == 2:
                if x < root.left.value:
                    root = SingleLeft(root)
                else:
                    root.left = DoubleLeft(root)
        elif root.value < x:
            root.right = Insert(x, root.right)
            if Height(root.right) - Height(root.left) == 2:
                if x > root.right.value:
                    root = SingleRight(root)
                else:
                    root.right = DoubleRight(root)
    root.height = max(Height(root.left), Height(root.right)) + 1
    return root


def Delete(x, root):
    if root is None:
        return None
    else:
        if root.value == x:
            if root.right is not None and root.left is not None:
                root.value = FindMin(root.right)
            else:
                if root.right is None:
                    root = root.left
                elif root.left is None:
                    root = root.rigth
    if root is not None:
        # TODO
        pass

    return root


if __name__ == '__main__':
    pass
