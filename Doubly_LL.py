class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
        
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        
    def insert_end(self,data):
        node=Node(data)
        if self.head==None:
            self.head=node
            return
        
        temp=self.head
        while temp.next:
              temp=temp.next
#Correctly traverse to the last node first, then make chnages
        temp.next=node
        node.prev=temp
        node.next=None
    
    def Delete_fm_List(self,value):
        if self.head==None:
            return "Empty"
        temp=self.head
        while temp:
            if temp.data==value:
                break
            temp=temp.next
        if temp==None:
            return "Not Found"
        #Case1:If we're deleting head   
        if temp==self.head:
            self.head=temp.next 
            if self.head:
                self.head.prev=None
        else:
            if temp.prev:
                temp.prev.next = temp.next
            if temp.next:
                temp.next.prev = temp.prev

        print(f"\n{value} deleted successfully.\n")

        
    
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="<->")
            temp=temp.next
        print(None,end="\n")
    
dll = DoublyLinkedList()

dll.insert_end(10)
dll.insert_end(20)
dll.insert_end(30)
dll.insert_end(40)

print("Original List:")
dll.display()

dll.Delete_fm_List(30)

print("After deleting 30:")
dll.display()

dll.Delete_fm_List(10)

print("After deleting 10:")
dll.display()