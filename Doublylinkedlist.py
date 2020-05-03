class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self,head = None):
        self.head = head

    def append(self,newNode):
        if(self.head):
            current = self.head
            while(current.next!=None):
                current = current.next

            newNode.prev = current
            current.next = newNode
            newNode.next = None
        else:
            self.head = newNode

    def displayList(self):
        current = self.head
        if (current == None):
            print("Nothing to display")
        else:
            while(current):
                print(current.value)
                current = current.next

    def insertNode(self,pos,newElement):
        current = self.head
        counter = 1
        if(pos==1):
            newElement.next = current
            current.prev = newElement
            self.head = newElement
        else:
            while(current and counter<pos):
                current = current.next
                counter+=1
            newElement.prev = current.prev
            current.prev.next = newElement
            newElement.next = current
            current.prev = newElement

    def deleteNode(self,pos):
        current =self.head
        counter = 1
        if pos==1:
            self.head = current.next
            current.next = None
            current.prev = None

        else:
            while(current and counter<pos):
                current = current.next
                counter+=1

            if(counter==pos):
                current.prev.next=None
            else:
                current.prev.next = current.next
                current.next.prev = current.prev











n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(9)
n5 = Node(6)

dll = DoublyLinkedList(n1)
dll.append(n2)
dll.append(n4)
dll.append(n3)
dll.insertNode(4,n5)
dll.displayList()
dll.deleteNode(5)
print("After deleting the node")
dll.displayList()


