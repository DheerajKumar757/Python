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
        i = 10
        while node:
            yield node
            node = node.next
            i = i-1
            if i == 0:
                break
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
def disp():
    i = 10
    SllLst = []
    for node in singlyLinkedList:
        SllLst.append(node.value)
        i = i-1
        if i == 0:
            break   
    print(SllLst)            

singlyLinkedList = SLinkedList()
node1 = Node(5)
singlyLinkedList.head = node1
singlyLinkedList.tail = node1
disp()
singlyLinkedList.insertSLL(12 ,10) # initially index does not matter disp()
singlyLinkedList.insertSLL(9 ,-1)
disp()
singlyLinkedList.insertSLL(50 ,2)
disp()
singlyLinkedList.insertSLL(100 ,0)
disp()
singlyLinkedList.insertSLL(100 ,0)
disp()
singlyLinkedList.transverseSLL()
