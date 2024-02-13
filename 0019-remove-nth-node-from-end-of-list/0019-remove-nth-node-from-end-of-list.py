# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        cnt=0
        temp=head
        while temp is not None:
            cnt+=1
            temp=temp.next
        if cnt==n:
            new_head=head.next
            head=None
            return new_head
        res=cnt-n
        temp=head
        while temp is not None:
            res-=1
            if res==0:
                break
            temp=temp.next
        del_node=temp.next
        temp.next=temp.next.next
        del_node=None
        return head