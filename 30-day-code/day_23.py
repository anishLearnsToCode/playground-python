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

    def levelOrder(self, root: Node):
        queue = []
        queue.append(root)

        while queue:
            current = queue.pop(0)
            if current is None:
                continue
            print(current.data, end=' ')
            queue.append(current.left)
            queue.append(current.right)
