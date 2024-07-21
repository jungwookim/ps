
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # iterative
        if not head:
            return
        
        prev = None
        cur = head

        while cur:
            next_temp = cur.next
            cur.next = prev
            prev = cur
            cur = next_temp

        return prev

        # recursive
        # if head is None or head.next is None:
        #     return head
        # reversed_head = self.reverseList(head.next)
        
        # head.next.next = head
        # head.next = None

        # return reversed_head
