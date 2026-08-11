# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # Anchor for the reversed list
        curr = head

        while curr:
            nxt = curr.next  # 1. Save remaining list

            # 2. Insert curr right after dummy
            curr.next = dummy.next
            dummy.next = curr

            curr = nxt  # 3. Move to the next node in original list

        return dummy.next