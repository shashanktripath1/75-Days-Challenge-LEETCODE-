# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=[]
        temp=head
        while temp is not None:
            stack.append(temp.val)
            temp=temp.next
        stack=sorted(stack)
        temp=head
        i=0
        while temp is not None:
            temp.val=stack[i]
            temp=temp.next
            i+=1
        return head
    #Brute Force
    #TC=O(N+NlogN+N)
    #SC=O(N)
        