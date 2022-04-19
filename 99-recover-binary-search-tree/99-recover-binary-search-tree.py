# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        list=[]
        def inorder(node):
            if node is not None:
                inorder(node.left)
                list.append(node)
                inorder(node.right)
        inorder(root)
        N=len(list)
        first_node=list[0]
        last_node=list[-1]
        
        for i in range(1,N):
            if list[i].val<list[i-1].val:
                first_node=list[i-1]
                break
        for i in range(N-2,-1,-1):
            if list[i].val>list[i+1].val:
                last_node=list[i+1]
                break
        first_node.val,last_node.val=last_node.val,first_node.val
                
                
        