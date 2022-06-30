# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        current=dummy=ListNode(0)
        while list1 and list2:
            if list1.val<list2.val:
                current.next=list1
                list1=list1.next
            else:
                current.next=list2
                list2=list2.next
            current=current.next
        if list1:
            current.next=list1
        if list2:
            current.next=list2
        return dummy.next
     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
            if len(lists)==0:
                return None
            elif len(lists)==1:
                return lists[0]
            else:
                output=lists[0]
                for i in range(1,len(lists)):
                    output=self.mergeTwoLists(output,lists[i])
            return output