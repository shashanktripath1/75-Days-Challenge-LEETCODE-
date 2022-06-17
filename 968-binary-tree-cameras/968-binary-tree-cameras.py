class Solution:
   
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        def postorder(v):
            if not v: return True, False
            left_covered, left_installed = postorder(v.left)
            right_covered, right_installed = postorder(v.right)
            if not left_covered or not right_covered:
                self.count += 1
                return True, True
            else:
                if left_installed or right_installed:
                    return True, False
                else:
                    return False, False
        covered, installed = postorder(root)
        return self.count + (not covered)