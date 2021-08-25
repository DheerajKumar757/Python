# do not insert value out of index
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    #insert in linked list
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                    if tempNode == self.tail:
                        newNode.next = None
                        self.tail.next = newNode
                        self.tail = newNode
                        break
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                

singlyLinkedList = SLinkedList()
node1 = Node(1)
node2 = Node(2)

singlyLinkedList.head = node1
singlyLinkedList.head.next = node2
singlyLinkedList.tail = node2
print([node.value for node in singlyLinkedList])
singlyLinkedList.insertSLL(5, 0)
print([node.value for node in singlyLinkedList])
singlyLinkedList.insertSLL(10, 2)
print([node.value for node in singlyLinkedList])
singlyLinkedList.insertSLL(50, -1)
print([node.value for node in singlyLinkedList])
singlyLinkedList.insertSLL(100, 0)
print([node.value for node in singlyLinkedList])
singlyLinkedList.insertSLL(200, 3)
print([node.value for node in singlyLinkedList])
singlyLinkedList.insertSLL(500, -1)
print([node.value for node in singlyLinkedList])
