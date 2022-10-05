class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            node = TreeNode(val, root)
            return node
        
        
        def dfs(node, val, depth):
            if not node:
                return
            
            if depth <= 1:
                return
            
            if depth == 2:
                left_node = TreeNode(val, node.left, None)
                right_node = TreeNode(val, None, right=node.right)
                node.left = left_node
                node.right = right_node
            
            dfs(node.left, val, depth-1)
            dfs(node.right, val, depth-1)
            
        dfs(root, val, depth)
        return root
