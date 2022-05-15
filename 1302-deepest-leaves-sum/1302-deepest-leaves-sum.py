class Solution:
    def __init__(self):
        self.total = 0
        self.depth = 0
        
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        def helperdepth(root):
            if not root:
                return 0
            return 1 + max(helperdepth(root.left), helperdepth(root.right))
        
        def helpersum(root,current):
            if root:
                if not root.left and not root.right and self.depth == current:
                    self.total += root.val
                helpersum(root.left, current + 1) 
                helpersum(root.right, current + 1)
            else:
                return
            
        self.depth = helperdepth(root)
        helpersum(root, 1)
        
        return self.total