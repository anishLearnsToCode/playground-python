class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data


class Solution:
    def insert(self,root,data):
        if root is None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self, root):
        return self.height(root) - 1

    def height(self, root: Node):
        if root is None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1
