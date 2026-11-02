class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def reverse(n):

            prev = None
            curr = n
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev

        newhead = reverse(head)

        dummy = ListNode(0, newhead)
        temp = dummy

        while n > 1:

            temp = temp.next
            newhead = newhead.next
            n -= 1

        if newhead and newhead.next:
            temp.next = newhead.next
        else:
            temp.next = None

        return reverse(dummy.next)