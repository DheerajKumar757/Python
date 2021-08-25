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
                    if tempNode == self.tail.next:
                        break
                    else:
                        tempNode = tempNode.next
                        index += 1
                if tempNode == self.tail.next:
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
                tempNode = tempNode.next        
                if tempNode == self.tail.next:
                    break

    # searching for a node in Circulr singly linked list
    def searchCSLL(self, nodeValue):
        if self.head is None:
            return 'There is not any node in this CSLL'
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return 'The node does not exist in CSLL'

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
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next        

    # delete entire CSLL
    def deleteEntireCSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None
        return 'CSLL has been deleted'            

# to insert element at the end use location as -1, last index will not work as of now here!
# we will update it soon thanks for your patiences
circularSLL = CircularSinglyLinkedList()
circularSLL.createCSLL(20)
circularSLL.traverseCSLL()
print([node.value for node in circularSLL])
circularSLL.insertCSLL(5, 0)
print([node.value for node in circularSLL])
print(circularSLL.insertCSLL(0, 5))
circularSLL.insertCSLL(10, -1)
print(circularSLL.insertCSLL(50, -1))
print([node.value for node in circularSLL])
circularSLL.insertCSLL(500, -1)
print([node.value for node in circularSLL])

print(circularSLL.deleteEntireCSLL())
print([node.value for node in circularSLL])
