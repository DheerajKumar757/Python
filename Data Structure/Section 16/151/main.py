class Node:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLindkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # creation of Doubly Linked List
    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return 'The DLL is created Successfully'

doublyLL = DoublyLindkedList()
print(doublyLL.createDLL(5))
print([node.value for node in doublyLL])

