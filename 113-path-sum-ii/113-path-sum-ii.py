class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans=[]
        if root is None:
            return 
        def helper(root,res):
            if root.left is None and root.right is None:
                res+="."+str(root.val)
                lst=list(map(int,res.lstrip(".").split(".")))
                if sum(lst)==targetSum:
                    ans.append(lst)
                return
            res+="."+str(root.val)
            if root.left: helper(root.left,res)
            if root.right: helper(root.right,res)
        helper(root,"")
        return ans