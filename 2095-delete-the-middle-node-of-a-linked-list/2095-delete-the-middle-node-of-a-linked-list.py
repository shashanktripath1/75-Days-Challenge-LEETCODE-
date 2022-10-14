# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        counter=0
        pointer1=pointer2=head
        while pointer1:
            counter+=1
            pointer1=pointer1.next
        mid=counter // 2
        for i in range(mid-1):
            pointer2=pointer2.next
        pointer2.next=pointer2.next.next
        return head

