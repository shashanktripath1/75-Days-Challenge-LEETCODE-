# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp=head
        node_set=set()
        while temp:
            if temp in node_set:
                return True
            
            node_set.add(temp)
            temp=temp.next
        return False
            