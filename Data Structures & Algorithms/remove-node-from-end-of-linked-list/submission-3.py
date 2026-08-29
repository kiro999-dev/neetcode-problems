# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
   
   
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if(not head.next):
            head = None
            return head
        dummy = ListNode()
        dummy.next = head
        l = dummy
        r = head
        N = 0
        while  N <n and r:
            N+=1
            r = r.next
        while r:
            l =l.next
            r = r.next
        l.next = l.next.next
        return dummy.next

       
