    # class Node:
    #     def __init__(self, val):
    #         self.val = val
    #         self.next = None


    # class MyLinkedList(object):
    #     def __init__(self):
    #         self.head = None
    #         self.size = 0

    #     def get(self, index: int) -> int:
    #         if index < 0 or index >= self.size:
    #             return -1

    #         current = self.head

    #         for _ in range(0, index):
    #             current = current.next

    #         return current.val

    #     def addAtHead(self, val: int) -> None:
    #         new_node=Node(val)
    #         new_node.next=self.head
    #         self.head=new_node
    #         self.size+=1

    #     def addAtTail(self, val: int) -> None:
    #         curr = self.head
    #         if curr is None:
    #             self.head = Node(val)
    #         else:
    #             while curr.next is not None:
    #                 curr = curr.next
    #             curr.next = Node(val)

    #         self.size += 1
                
            

    #     def addAtIndex(self, index: int, val: int) -> None:
    #         if index>self.size or index<0:
    #             pass
    #         if index==self.size:
    #             self.addAtTail(val)
    #         else:
    #             while(index>0):
    #                 self.head=self.head.next
    #                 index-=1
    #             self.addAtHead(val)

    #     def deleteAtIndex(self, index: int) -> None:
    #         if index>=self.size or index<0:
    #             pass
    #         prev=self.head 
    #         curr=self.head
    #         while(index>0):
    #             prev=curr
    #             curr=curr.next
    #             index-=1
    #         prev.next=curr.next
            


    # # Your MyLinkedList object will be instantiated and called as such:
    # # obj = MyLinkedList()
    # # param_1 = obj.get(index)
    # # obj.addAtHead(val)
    # # obj.addAtTail(val)
    # # obj.addAtIndex(index,val)
    # # obj.deleteAtIndex(index)