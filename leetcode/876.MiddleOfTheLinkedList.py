# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = []
        while head:
            result.append(head)
            head = head.next

        mid = len(result) // 2
        return result[mid]