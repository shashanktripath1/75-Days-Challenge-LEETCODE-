# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None or k==0:
            return head
        cnt_len=1
        temp=head
        while temp.next is not None:
            cnt_len+=1
            temp=temp.next
        temp.next = head
        k=k%cnt_len
        end=cnt_len-k
        while end:
            temp=temp.next
            end-=1
        head=temp.next
        temp.next=None
        return head
            
        