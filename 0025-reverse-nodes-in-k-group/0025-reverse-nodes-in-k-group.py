# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_ll(self,head):
        temp=head
        prev=None
        while temp is not None:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        return prev
    def find_kth(self,temp,k):
        k-=1
        while temp is not None and k>0:
            k-=1
            temp=temp.next
        return temp
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp=head
        prev_node=None
        while temp is not None:
            kth_node=self.find_kth(temp,k)
            if kth_node==None:
                if prev_node:
                    prev_node.next=temp
                    break
            next_node=kth_node.next
            kth_node.next=None
            self.reverse_ll(temp)
            if temp==head:
                head=kth_node
            else:
                prev_node.next=kth_node
            prev_node=temp
            temp=next_node
        return head
            