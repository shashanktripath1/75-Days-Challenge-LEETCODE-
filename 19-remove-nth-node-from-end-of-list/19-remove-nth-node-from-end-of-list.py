# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast=slow=head
        for i in range(n):
            fast=fast.next
        while fast is None:
            return head.next
        while fast.next is not None:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return head