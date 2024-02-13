# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if   not head.next:
            return None
        temp=head
        cnt=0
        while temp!=None:
            cnt+=1
            temp=temp.next
        n=cnt//2
        temp=head
        while temp!=None:
            n-=1
            if n==0:
                break
            temp=temp.next
        #del_node=temp.next
        temp.next=temp.next.next
        #del_node=None
        return head