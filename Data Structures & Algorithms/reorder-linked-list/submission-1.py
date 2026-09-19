# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

    # 1 -> 2 -> 3 -> 4 -> 5 -> 6

    #    1. find the half way point

        slow,fast = head,head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # use slow for the 2nd half


    #    2. reverse the second half
        prev = None

        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # now prev points to the end of the 2nd half

    #    3. merge the 2 halfs 

        curr = head

        while head and prev and head.next != prev:
            tmp1 = head.next
            head.next = prev
            head = tmp1
            tmp2 = prev.next
            prev.next = head
            prev = tmp2


        


        


