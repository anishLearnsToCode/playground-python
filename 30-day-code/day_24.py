class Node:
    def __init__(self,data):
        self.data = data
        self.next: Node = None


class Solution:
    def insert(self, head, data):
            p = Node(data)
            if head is None:
                head = p
            elif head.next is None:
                head.next = p
            else:
                start=head
                while start.next is not None:
                    start=start.next
                start.next=p
            return head
    def display(self, head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self, head: Node) -> Node:
        if head is None:
            return head

        current = head
        while current.next is not None:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
        return head
