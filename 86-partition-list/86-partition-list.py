# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        h1=small=ListNode(0)
        h2=high=ListNode(0)
        while head!=None:
            if head.val<x:
                small.next=head
                small=small.next
            else:
                high.next=head
                high=high.next
            head=head.next
        high.next=None
        small.next=h2.next
        return h1.next