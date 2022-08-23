# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ans=[]
        while head!=None:
            ans.append(head.val)
            head=head.next
        slow,fast=0,len(ans)-1
        for i in ans:
            if slow!=fast:
                ans[slow],ans[fast]=ans[fast],ans[slow]
            slow+=1
            fast-=1
        return ans==ans[::-1]
                