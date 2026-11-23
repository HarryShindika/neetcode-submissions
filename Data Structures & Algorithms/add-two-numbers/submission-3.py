# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        rem = 0
        curr1 = l1
        curr2 = l2
        res = ListNode(0,None)
        dummy = res

        while curr1 and curr2:
            total = curr1.val + curr2.val + rem

            dummy.next = ListNode(total % 10, None)
            rem = total // 10
            dummy = dummy.next

            curr1 = curr1.next
            curr2 = curr2.next


        if curr1:
            dummy.next = curr1
        else:
            dummy.next = curr2

        if rem > 0 and dummy.next:
            while dummy.next:
                total = dummy.next.val + rem
                dummy.next.val = total % 10
                rem = total // 10
                dummy = dummy.next
        
        if rem > 0:
            dummy.next = ListNode(rem, None)
            

        return res.next






        


        