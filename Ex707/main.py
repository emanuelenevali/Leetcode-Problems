# design of a linked list

# MyLinkedList() Initializes the MyLinkedList object.

# int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.

# void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, 
# the new node will be the first node of the linked list.

# void addAtTail(int val) Append a node of value val as the last element of the linked list.

# void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. 
# If index equals the length of the linked list, the node will be appended to the end of the linked list. 
# If index is greater than the length, the node will not be inserted.

# void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

class Node:
    # Node of a single linked list
    def __init__(self, val):
        self.val=val
        self.next=None

class MyLinkedList:

    def __init__(self):
        self.head=None
        self.size=0
        

    def get(self, index: int) -> int:
        if index<0 or index>=self.size:
            return -1
        curr=self.head
        for i in range(0, index):
            curr=curr.next
        return curr.val
               

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.size:
            return
        curr=self.head
        new_node=Node(val)
        if index==0:
            new_node.next=curr
            self.head=new_node
        else:
            for _ in range(index-1):
                curr=curr.next
            new_node.next=curr.next
            curr.next=new_node
        
        self.size+=1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        curr=self.head
        if curr == None:
            return
        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(0, index-1):
                curr = curr.next
            curr.next = curr.next.next

        self.size-=1