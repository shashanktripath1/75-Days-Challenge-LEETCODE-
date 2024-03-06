# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,level,ds):
        if not root:
            return
        if level==len(ds):
            ds.append(root.val)
        self.dfs(root.right,level+1,ds)
        self.dfs(root.left,level+1,ds)
        
    
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level=0
        ds=[]
        self.dfs(root,level,ds)
        return ds
            