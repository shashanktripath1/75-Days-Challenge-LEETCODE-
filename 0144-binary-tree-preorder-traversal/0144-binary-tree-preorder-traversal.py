# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#iterative preorder
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack=[]
        if not root:
            return []
        ans=[]
        stack.append(root)
        while stack:
            stack_len=len(stack)
            for i in range(stack_len):
                cur=stack.pop()
                ans.append(cur.val)
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
        return ans