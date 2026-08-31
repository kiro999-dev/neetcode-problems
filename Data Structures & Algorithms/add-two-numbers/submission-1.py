# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        resListe = None
        dummy = ListNode()
        resListe = dummy
        temp = resListe
        carry = 0
        val = 0
        resSum = 0
        while l1 or l2:
            if(l1 and l2):
                resSum = l1.val + l2.val + carry
            if(l1 and not l2):
                resSum = l1.val + 0 + carry
            if(not l1 and  l2):
                resSum = 0 + l2.val + carry
            carry = 0
            val = resSum % 10
            if(resSum >= 10):
                carry = 1
            temp.next = ListNode(val)
            temp = temp.next
            if(l1):
             l1 = l1.next
            if(l2):
             l2 = l2.next
        if(carry !=0):
            temp.next = ListNode(carry)

        return dummy.next