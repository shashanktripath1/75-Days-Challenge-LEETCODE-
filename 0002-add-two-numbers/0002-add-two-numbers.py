# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        temp=dummy
        carry=0
        while l1 is not None or l2 is not None or carry:
            sum1=0
            if l1 is not None:
                sum1+=l1.val
                l1=l1.next
            if l2 is not None:
                sum1+=l2.val
                l2=l2.next
            sum1+=carry
            carry=sum1//10
            node=ListNode(sum1%10)
            temp.next=node
            temp=temp.next
        return dummy.next
            