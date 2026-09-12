
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Linked_List:
    def __init__(self):
        self.head=None
        
    #Insertion @ the beginning
    def Insert_at_start(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    # Insert at end
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        new_node.next=None
        
    # Insert after a given value
    def insert_at_given_posn(self,data,key):
        temp=self.head
        
        while temp:
            if temp.data==key:
               new_node=Node(data)
               new_node.next=temp.next
               temp.next=new_node
               return
            temp=temp.next
    
        # Display list
    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")

            temp = temp.next

        print("Key doesn't exist!")

# if __name__=='__main__':

ll = Linked_List()

ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)

print("Original List:")
ll.display()

ll.Insert_at_start(5)
print("After inserting at beginning:")
ll.display()

ll.insert_at_end(40)
print("After inserting at end:")
ll.display()

ll.insert_at_given_posn(25, 20)
print("After inserting 25 after 20:")
ll.display()

                
        
        
