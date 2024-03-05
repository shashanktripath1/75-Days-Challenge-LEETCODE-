# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#left right root
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        stack1=[root]
        stack2=[]
        while stack1:
            cur=stack1.pop()
            stack2.append(cur.val)
            if  cur.left:
                stack1.append(cur.left)
            if cur.right:
                stack1.append(cur.right)
        ans=[]
        while stack2:
            element=stack2.pop()
            ans.append(element)
        return ans