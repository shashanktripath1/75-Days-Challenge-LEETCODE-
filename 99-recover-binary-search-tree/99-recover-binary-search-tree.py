# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        bucket=[]
        def inorder(node):
            if node!=None:
                inorder(node.left)
                bucket.append(node)
                inorder(node.right)
        inorder(root)
        
        N=len(bucket)
        firstnode=bucket[0]
        lastnode=bucket[-1]
        
        for i in range(1,N):
            if bucket[i].val < bucket[i-1].val:
                firstnode=bucket[i-1]
                break
        for i in range(N-2,-1,-1):
            if bucket[i].val>bucket[i+1].val:
                lastnode=bucket[i+1]
                break
        firstnode.val,lastnode.val=lastnode.val,firstnode.val
        
        