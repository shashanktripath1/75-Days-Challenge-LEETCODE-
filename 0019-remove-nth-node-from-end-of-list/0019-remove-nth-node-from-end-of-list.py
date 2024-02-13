# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast=head
        for i in range(n):
            fast=fast.next
        if fast is None:
            return head.next
        slow=head
        while fast.next is not None:
            slow=slow.next
            fast=fast.next
        del_node=slow.next
        slow.next=slow.next.next
        del_node=None
        return head