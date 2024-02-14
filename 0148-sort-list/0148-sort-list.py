# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge_ll(self,left,right):
        temp=ans=ListNode()
        while left!=None and right!=None:
            if left.val<=right.val:
                temp.next=left
                left=left.next
            else:
                temp.next=right
                right=right.next
            temp=temp.next
        if left is not None:
            temp.next=left
            #left=left.next
        if right is not None:
            temp.next=right
            #right=right.next
        return ans.next
            
    def middle(self,head):
        slow=head
        fast=head.next #to handle the edge case
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        left=head
        right=self.middle(head)
        temp=right.next
        right.next=None
        right=temp
        left=self.sortList(left)
        right=self.sortList(right)
        return self.merge_ll(left,right)
    #optimal approach using merge sort
    #TC=O(logN*(N+N/2))
    #SC=O(logN) - For Recursive Stack Space
    