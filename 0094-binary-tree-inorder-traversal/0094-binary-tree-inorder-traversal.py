# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# left root right
#Morris traversal
#check its previous submission for all comments
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        cur=root
        while cur!=None:
            if not cur.left:
                ans.append(cur.val)
                cur=cur.right
            else:
                temp=cur
                temp=temp.left
                while temp.right and temp.right!=cur:
                    temp=temp.right
                if not temp.right:
                    temp.right=cur
                    cur=cur.left
                else:
                    ans.append(cur.val)
                    temp.right=None
                    cur=cur.right
        return ans