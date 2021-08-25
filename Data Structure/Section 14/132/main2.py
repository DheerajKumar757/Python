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
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    if tempNode == self.tail:             
                        break
                    tempNode = tempNode.next
                    index += 1
                if tempNode == self.tail:
                    self.tail.next = newNode
                    self.tail = newNode
                else:
                    nextNode = tempNode.next
                    tempNode.next = newNode
                    newNode.next = nextNode
    def transverseSLL(self):
        if self.head is None:
            print('The singly linked does not exist')
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
    
    # search for a node in singly linked list
    def searchSLL(self, nodeValue):
        loc = -1
        if self.head is None:
            return 'The list does not exist',loc
        else:
            node = self.head
            loc = 0
            while node is not None:
                if node.value == nodeValue:
                    return node.value, loc
                node = node.next
                loc = loc + 1
            return "The value does not exist in the list.", loc
                

singlyLinkedList = SLinkedList()
singlyLinkedList2 = SLinkedList()
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
singlyLinkedList.insertSLL(100,50)
print([node.value for node in singlyLinkedList])
singlyLinkedList.insertSLL(200, 3)
print([node.value for node in singlyLinkedList])
singlyLinkedList.insertSLL(500, -1)
print([node.value for node in singlyLinkedList])
#singlyLinkedList.transverseSLL()

print(singlyLinkedList2.searchSLL(300))
print(singlyLinkedList.searchSLL(10))
print(singlyLinkedList.searchSLL(300))
