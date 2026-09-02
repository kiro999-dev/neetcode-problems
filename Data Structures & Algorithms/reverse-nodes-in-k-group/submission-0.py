# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getKthNode(self,curr,k):
        while curr and k > 0:
            curr = curr.next
            k-=1
        return curr
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0,head)
        groupPrev = dummy
        while True:
            Kth = self.getKthNode(groupPrev,k)
            if(not Kth):
                break
            groupNext = Kth.next

            prev,curr = groupNext,groupPrev.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev =curr
                curr = temp
            tmp = groupPrev.next
            groupPrev.next = Kth
            groupPrev = tmp
        return dummy.next
        