class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        freq = defaultdict(int)
        
        def pal_count(node: Optional[TreeNode], odd_freq_count: int):
            if not node: return 0
            
            node_val = node.val
            freq[node_val] += 1
            
            if freq[node_val] % 2 != 0:
                odd_freq_count += 1
            else:
                odd_freq_count -= 1
                
            if not node.left and not node.right:
                freq[node_val] -= 1
                
                if odd_freq_count <= 1:
                    return 1
                return 0
            
            ans = pal_count(node.left, odd_freq_count) + pal_count(node.right, odd_freq_count)
            
            
            freq[node_val] -= 1
            
            return ans
            
            
        return pal_count(root, 0)