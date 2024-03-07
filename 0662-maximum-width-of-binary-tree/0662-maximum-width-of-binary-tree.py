class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([[root, 0]])
        max_width = 0
        
        while queue:
            size = len(queue)
            _, left_idx = queue[0]
            _, right_idx = queue[-1]
            
            width = right_idx - left_idx + 1
            max_width = max(max_width, width)
            
            for i in range(size):
                node, ind = queue.popleft()
                
                if node.left:
                    queue.append([node.left, 2 * ind + 1])
                if node.right:
                    queue.append([node.right, 2 * ind + 2])
                    
        return max_width
