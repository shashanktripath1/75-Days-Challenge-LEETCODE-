# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d=defaultdict(list)
        queue=deque()
        queue.append([root,0,0])
        while queue:
            node,row,col=queue.popleft()
            d[col].append([node.val,row])
            if node.left:
                queue.append([node.left,row+1,col-1])
            if node.right:
                queue.append([node.right,row+1,col+1])
        ans=[]
        for i in sorted(d.keys()):
            lst=d[i]
            lst.sort(key=lambda x:(x[1],x[0]))
            temp=[]
            for i in lst:
                temp.append(i[0])
            ans.append(temp)
        return ans