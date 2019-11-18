class AvlNode(object):
    def __init__(self, left = None, right = None, data = None, height = 0):
        self.left = left
        self.right = right
        self.height = height
        self.data = data


class AvlTree(object):

    def __init__(self):
        self.tree = None

    def height(self, node):
        if node is None:
            return -1
        else:
            return 1 + max(self.height(node.left), self.height(node.right))

    def rotateFromRight(self, t):
        tmp = t.right
        t.right = tmp.left
        tmp.left = t
        t = tmp
        return t

    def doubleRotateFromRight(self, t):
        t.right = self.rotateFromLeft(t.right)
        t = self.rotateFromRight(t)
        return t

    def rotateFromLeft(self, t):
        tmp = t.left
        t.left = tmp.right
        tmp.right = t
        t = tmp
        return t

    def doubleRotateFromLeft(self, t):
        t.left = self.rotateFromRight(t.left)
        t = self.rotateFromLeft(t)
        return t

    def insert(self, t, key):
        if t is None:
            t = AvlNode(data=key)
        else:
            if t.data[0] == key:
                return t
            if t.data[0] > key[0]:
                t.left = self.insert(t=t.left, key=key)
                if self.height(t.left) - self.height(t.right) == 2:
                    if t.left.data[0] > key[0]:
                        t = self.rotateFromLeft(t)
                    else:
                        t = self.doubleRotateFromLeft(t)

            if t.data[0] < key[0]:
                t.right = self.insert(t=t.right, key=key)
                if self.height(t.right) - self.height(t.left) == 2:
                    if t.right.data[0] < key[0]:
                        t = self.rotateFromRight(t)
                    else:
                        t = self.doubleRotateFromRight(t)

        t.height = max(self.height(t.left), self.height(t.right)) + 1
        return t

    def preOrder(self, root):

        if not root:
            return

        print("{0} ".format(root.data[0]), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

