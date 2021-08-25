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

    def insertCSLL(self, value, location):
        if self.head is None:
            return "The head reference is none"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next  = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    if tempNode == self.tail:
                        break
                    else:
                        tempNode = tempNode.next
                        index += 1
                if tempNode == self.tail:
                    return 'Location is out of range'
                else:
                    nextNode = tempNode.next
                    tempNode.next = newNode
                    newNode.next = nextNode
            return 'Node has been successfully inserted!'
    
    # Traversal of CSLL
    def traverseCSLL(self):
        if self.head is None:
            print('There is no element for traversal')
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)            
                if tempNode == self.tail:
                    break
                else:
                    tempNode = tempNode.next

    # searching for a node in Circulr singly linked list
    def searchCSLL(self, nodeValue):
        if self.head is None:
            return 'There is not any node in this CSLL'
        else:
            index = 0
            tempNode = self.head
            while tempNode:  
                if tempNode == self.tail:
                    if tempNode.value == nodeValue:
                        return tempNode.value, index
                    else:
                        return 'The node does not exist in CSLL'
                else:
                    if tempNode.value == nodeValue:
                        return tempNode.value, index
                    else:
                        tempNode = tempNode.next
                        index += 1

    # Delete a node from circular singly linked list
    def deleteNodeCSLL(self, location):
        if self.head is None:
            print('There is not any node in CSLL')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    tempNode = self.head
                    while tempNode is not None:
                        if tempNode.next == self.tail:
                            break
                        tempNode = tempNode.next
                    tempNode.next = self.head
                    self.tail = tempNode
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    if tempNode == self.tail:
                        break
                    else:
                        tempNode = tempNode.next
                        index += 1
                if tempNode == self.tail:
                    return 'Index is Out of range'
                else:
                    nextNode = tempNode.next
                    tempNode.next = nextNode.next  






circularSLL = CircularSinglyLinkedList()
circularSLL.createCSLL(20)
print(circularSLL.searchCSLL(20))
print([node.value for node in circularSLL])
circularSLL.insertCSLL(5, 0)
print([node.value for node in circularSLL])
print(circularSLL.insertCSLL(0, 5))
circularSLL.insertCSLL(10, -1)
print([node.value for node in circularSLL])
print(circularSLL.insertCSLL(0, 5))
print(circularSLL.insertCSLL(40, 2))
print([node.value for node in circularSLL])

circularSLL.deleteNodeCSLL(0)
print([node.value for node in circularSLL])
circularSLL.deleteNodeCSLL(1)
print([node.value for node in circularSLL])
circularSLL.deleteNodeCSLL(-1)
print([node.value for node in circularSLL])
circularSLL.deleteNodeCSLL(0)
print([node.value for node in circularSLL])
circularSLL.deleteNodeCSLL(0)
print([node.value for node in circularSLL])