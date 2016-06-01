
class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def __lt__(self, other):
        if other is not None:
            return self.key < other.key
        return super().__lt__(other)

    def ___le__(self, other):
        if other is not None:
            return self.key <= other.key
        return super().__le__(other)

    def __eq__(self, other):
        if other is not None:
            return self.key == other.key
        return super().__eq__(other)

    def __ne__(self, other):
        if other is not None:
            return self.key != other.key
        return super().__ne__(other)

    def __gt__(self, other):
        if other is not None:
            return self.key > other.key
        return super().__gt__(other)

    def __ge__(self, other):
        if other is not None:
            return self.key >= other.key
        return super().__ge__(other)

