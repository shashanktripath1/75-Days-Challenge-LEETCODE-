# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Target node is replaced by largest element of left subtree
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
        if not root:
            return None
            
        if root.val > key:
		    # Target node is smaller than currnet node, search left subtree
			
            root.left = self.deleteNode( root.left, key )

        elif root.val < key:
		    # Target node is larger than currnet node, search right subtree
			
            root.right = self.deleteNode( root.right, key )

        else:
            # Current node is target node
			
            if (not root.left) or (not root.right):
                # At least one child is empty
                # Target node is replaced by either non-empty child or None
                root = root.left if root.left else root.right

            else:
                # Both two childs exist
                # Target node is replaced by largest element of left subtree
                cur = root.left

                while cur.right:
                    cur = cur.right

                root.val = cur.val
                root.left = self.deleteNode( root.left, cur.val )
                    
        return root