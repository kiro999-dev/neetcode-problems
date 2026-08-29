# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getTail(self,head:Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while temp and temp.next and temp.next.next:
            temp = temp.next
        tail = None
        if(temp):
            tail = temp.next
            temp.next = None
        return tail
    def reorderList(self, head: Optional[ListNode]) -> None:
        beg = head
        tail = None
        NEXT = head
        while(NEXT and NEXT.next and beg != tail ):
            tail = self.getTail(head)
            NEXT=beg.next
            beg.next = tail
            tail.next  = NEXT
            beg = tail.next
        return