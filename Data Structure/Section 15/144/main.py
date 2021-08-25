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
                    





circularSLL = CircularSinglyLinkedList()
circularSLL.createCSLL(20)
circularSLL.traverseCSLL()
print([node.value for node in circularSLL])
circularSLL.insertCSLL(5, 0)
print([node.value for node in circularSLL])
print(circularSLL.insertCSLL(0, 5))
circularSLL.insertCSLL(10, -1)

print([node.value for node in circularSLL])
circularSLL.traverseCSLL()
