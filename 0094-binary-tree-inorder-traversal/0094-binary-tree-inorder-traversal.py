# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# left root right
#Morris traversal
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        cur = root
        while cur != None:
            #printing the leftmost node
            if not cur.left:
                ans.append(cur.val)
                cur = cur.right
            else:
                temp = cur
                temp = temp.left
                #going to the rightmost node in the left subtree (lets call it temp)
                while temp.right and temp.right != cur:
                    temp = temp.right
                
                #2 conditions arise:
                
                #i. the right child of temp doesn't exist (The thread to the cur node has not been made)
                #in this case, point the right child of temp to cur and move cur to its left child
                if not temp.right:
                    temp.right = cur
                    cur = cur.left

                #ii. the thread has already been created so we break the thread
                #(pointing the temp's right child back to None)and print cur.
                #Finally, move cur to its right child      
                else:
                    ans.append(cur.val)
                    temp.right = None
                    cur = cur.right

        return ans