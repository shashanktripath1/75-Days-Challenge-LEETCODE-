class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        lst=[]
        def inorder(root):
            if not root: return 
            inorder(root.left)
            lst.append(root.val)
            inorder(root.right)
        inorder(root)
        ans=TreeNode(-1)
        root=ans
        while lst:
            temp=TreeNode(lst.pop(0))
            ans.right=temp
            ans=ans.right
        return root.right