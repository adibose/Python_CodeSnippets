class node:
    def __init__(self,value):
        self.value = value
        self.next = None

class CircularLinkList:
    def __init__(self,head = None):
        self.head = head
        current = self.head
        current.next = self.head

    def append(self,new_element):
        current =self.head
        if(current):
            while(current.next!=self.head):
                current = current.next

            current.next = new_element
            new_element.next = self.head
    def displayList(self):
        if(self.head):
            current = self.head
        while(current.next!=self.head):
            print(current.value)
            current=current.next

        print(current.value)





class linklist:
    def __init__(self,head = None):
        self.head = head

    def append(self,new_element):

        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def display_list(self):
            current = self.head
            while current:
                print(current.value)
                current = current.next

    def display_reverse(self):
        prev = None
        current = self.head
        if current!= None:
            while current:
                nextNode = current.next
                current.next = prev
                prev = current
                current = nextNode
            self.head = prev
    #For Stack
    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        new_element.next = self.head
        self.head = new_element
    #For Stack
    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        deleted = self.head
        if self.head:
            self.head = self.head.next
            deleted.next = None
            return deleted
        else:
            return None


    def get_node_in_position(self,position):
        counter = 1
        current = self.head
        if(position<1):
            return None

        while(current and counter<=position):
            if counter==position:
                print(current.value)
            current = current.next
            counter+=1

    def get_pos_of_node(self,value):
        counter = 1
        current = self.head

        while(current):
            if current.value == value:
                print(counter)
            current = current.next
            counter+=1

    def get_mid_node(self):
        slow = self.head
        fast = self.head

        if(self.head != None):
            while(fast and fast.next!=None):
                slow=slow.next
                fast=fast.next.next
            return slow.value
        else:
            return slow.value




    def insert_node(self,pos,new_element):
        current = self.head
        counter= 1
        if pos > 1:
            while(current and counter < pos):
                if(counter == pos - 1):
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif pos == 1:
            new_element.next = self.head
            self.head = new_element

    def del_node(self,element):
        current = self.head

        if current.value != element:
            while(current):
                prev = current
                current = current.next
                if(current.value == element):
                    prev.next = current.next
                    break
        else :
            self.head = current.next

    def delAllNodes(self):
        current = self.head
        while(current):
            deleted = current
            current = current.next
            self.head = current
            deleted.next = None
            print("Node deleted :", deleted.value)

    def detectLoop(self):
        counter = 0
        slow = self.head
        fast = self.head

        while(slow and fast and fast.next):
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                counter = 1
                print("Loop Detected")
                break
        if counter == 0:
            print("No loop")



n1 = node(1)
n2 = node(2)
n3 = node(3)
n4 = node(4)
n5 = node(5)
n6 = node(6)


cll = CircularLinkList(n1)
cll.append(n3)
cll.displayList()

# ll = linklist(n1)
# ll.append(n2)
# ll.append(n3)
# ll.append(n4)
# ll.append(n5)
# ll.append(n6)

# ll.display_list()

#print(ll.get_mid_node())
#ll.display_reverse()
# ll.display_list()
# ll.delAllNodes()
# ll.display_list()




# n1 = node(1)
# n2 = node(2)
# n3 = node(3)
# n4 = node(32)
# n5 = node(22)
# n6 = node(75)
# ll = linklist(n1)
# ll.append(n2)
# ll.append(n3)
# ll.append(n4)
# ll.append(n5)
#
# ll.insert_node(2,n6)
#
# ll.display_list()
# ll.del_node(22)
# print("------------------")
# ll.display_list()