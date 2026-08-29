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
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = slow.next
        b1 = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        b2 = self.reverseList(slow.next)
        slow.next = None
        while(b2):
            temp1 = b1.next
            temp2 = b2.next
            b1.next = b2
            b2.next = temp1
            b1 = temp1
            b2 = temp2

        return