# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False

        forward_stack, backward_stack = [], []
        forward_ptr, backward_ptr = root, root

        while True:
            while forward_ptr:
                forward_stack.append(forward_ptr)
                forward_ptr = forward_ptr.left

            while backward_ptr:
                backward_stack.append(backward_ptr)
                backward_ptr = backward_ptr.right

            if not forward_stack or not backward_stack:
                break

            forward_node, backward_node = forward_stack[-1], backward_stack[-1]

            if forward_node == backward_node:
                break

            current_sum = forward_node.val + backward_node.val

            if current_sum == k:
                return True
            elif current_sum < k:
                forward_ptr = forward_stack.pop().right
            else:
                backward_ptr = backward_stack.pop().left

        return False
