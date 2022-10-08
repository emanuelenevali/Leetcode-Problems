# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode()
        ret = res
        current1 = l1
        current2 = l2
        reminder = 0
        flag1 = 0
        flag2 = 0
        while True:
            digits_sum = current1.val-flag1+current2.val-flag2+reminder
            res.val = digits_sum%10
            reminder = int(digits_sum/10)
            if current1.next == None and current2.next == None:
                if reminder != 0:
                    res.next = ListNode(reminder)
                break
            if current1.next != None:
                current1 = current1.next
            else:
                flag1 = current1.val
            if current2.next != None:
                current2 = current2.next
            else:
                flag2 = current2.val          
            res.next = ListNode()
            res = res.next
        return ret