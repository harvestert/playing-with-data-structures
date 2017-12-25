class ListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        # If head is empty, set head
        if self.head is None:
            self.head = ListNode(value)
            return

        # Otherwise, find last node
        node = self.head
        while node.next is not None:
            node = node.next

        # Add after the last node
        node.next = ListNode(value)

    def delete(self, value):
        prev = None
        current = self.head

        while current is not None:
            if current.value == value:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return

            prev = current
            current = current.next

    def size(self):
        count = 0

        node = self.head
        while node is not None:
            count += 1
            node = node.next

        return count
