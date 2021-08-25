class Node:
    def __init__(self, Value=None):
        self.value = Value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.tail.next:
                break
            node = node.next

    # creation of circular singly linked list
    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return 'The CSLL has been created'

circularSLL = CircularSinglyLinkedList()
circularSLL.createCSLL(10)

print([node.value for node in circularSLL])
