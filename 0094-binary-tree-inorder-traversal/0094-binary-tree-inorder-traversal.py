# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# left root right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans,stack=[],[]
        cur=root
        while stack or cur:
            if cur:
                stack.append(cur)
                cur=cur.left
            else:
                cur=stack.pop()
                ans.append(cur.val)
                cur=cur.right
        return ans