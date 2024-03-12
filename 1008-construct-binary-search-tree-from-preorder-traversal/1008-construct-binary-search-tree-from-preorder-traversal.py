# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def BUILDBST(self,ind,start,end,preorder):
        if ind[0]==len(preorder) or not (start<=preorder[ind[0]]<=end):
            return None
        node_val=preorder[ind[0]]
        ind[0]+=1
        root=TreeNode(node_val)
        root.left=self.BUILDBST(ind,start,node_val,preorder)
        root.right=self.BUILDBST(ind,node_val,end,preorder)
        return root
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        ind=[0]
        return self.BUILDBST(ind,float('-inf'),float('inf'),preorder)