# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while(curr):
            Next = curr.next
            curr.next = prev
            prev = curr
            curr = Next
        return prev
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if(not head.next):
            head = None
            return head
        i = 1
        head =  self.reverseList(head)
        if(n==1):
            head = head.next
            return self.reverseList(head)
        curr = head
        deleted = None
        while i < n-1  and curr:
            curr = curr.next
            i+=1
        deleted = curr.next
        curr.next = deleted.next
        deleted.next = None
        return self.reverseList(head)
