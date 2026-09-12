class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class CircularLinkedList:
    def __init__(self):
           self.head = None

    def insert_end(self, data):
        node = Node(data)

        # If list is empty
        if self.head is None:
            self.head = node
            node.next = self.head # Points back 2 itself(circular fashion)
            return
        
        temp=self.head
        while temp.next!=self.head:
            temp=temp.next
        temp.next=node
        node.next=self.head
        
    def delete(self,value):
        if self.head is None:
            return "empty"
        temp=self.head
        prev=None
        #Are we deleting the head node in the list?

        if self.head.data==value:
            # Are we deleting the only node in the list?
            if self.head.next==self.head:
                self.head.next=None
                print(f"{value} has been deleted")    
                return
                # Deleting any given node
        prev = self.head
        temp = self.head.next

        while temp != self.head:
            if temp.data == value:
                prev.next = temp.next
                print(f"{value} has been deleted.")
                return
            prev = temp
            temp = temp.next

        return "Not found."
    
    def delete_end(self):
        if self.head is None:
            return " empty"

        if self.head.next == self.head:
            self.head = None
            return

        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next
        temp.next = self.head
    
    def printInfo(self):
        if self.head is None:
            return "empty"

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(Head)")


# Driver code
cll = CircularLinkedList()

cll.insert(10)
cll.insert(20)
cll.insert(30)
cll.insert(40)

print("Actual Circular Linked List:")
cll.display()

cll.delete(30)

print("After 30 is deleted:")
cll.display()

cll.delete(10)

print("After deleting 10:")
cll.display()
cll.delete_end()
print("After last node is deleted:")
cll.printInfo()