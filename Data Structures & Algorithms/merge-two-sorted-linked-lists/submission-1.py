# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if(list1 and not list2):
            return list1
        elif(list2 and not list1):
            return list2
        elif(not list1 and not list2):
            return None
            
        resList = ListNode(min(list1.val,list2.val))
        if(list1.val <= list2.val):
            list1 = list1.next
        else:
            list2 = list2.next
        temp = resList
        while list1 and list2:
            node = None
            if(list1.val <= list2.val):
                node = ListNode(list1.val)
                list1 = list1.next
            else:
                node = ListNode(list2.val)
                list2 = list2.next
            temp.next=node
            temp = temp.next
        if (list1):
            temp.next = list1
        if(list2):
            temp.next = list2
        return resList             

