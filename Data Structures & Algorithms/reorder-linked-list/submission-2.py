# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

    # 1 -> 2 -> 3 -> 4 -> 5 -> 6

    #    1. find the half way point

        slow,fast = head,head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # use slow for the 2nd half


    #    2. reverse the second half
        second = slow.next

        prev = None

        #  to cut off the 2 halfs
        slow.next = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # now prev points to the end of the 2nd half

    #    3. merge the 2 halfs 

        first, second = head,prev

        while second:
            tmp1,tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

        


        


