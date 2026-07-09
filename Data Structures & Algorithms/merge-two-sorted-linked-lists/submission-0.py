# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        while list1 is not None and list2 is not None:
            l1 = list1.val
            l2 = list2.val
            if l1 <= l2:
                cur.next = list1 #assign cur to point to list1 current node
                list1 = list1.next #point to next node in list1
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next # move pointer forward
        
        if list1 is not None:
            cur.next = list1
        
        elif list2 is not None:
            cur.next = list2
        return dummy.next
