# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mark_parents(self, root, parent_track):
        queue = deque()
        queue.append(root)
        while queue:
            cur = queue.popleft()
            if cur.left:
                parent_track[cur.left.val] = cur
                queue.append(cur.left)
            if cur.right:
                parent_track[cur.right.val] = cur
                queue.append(cur.right)

    def distanceK(self, root: Optional[TreeNode], target: Optional[TreeNode], k: int) -> List[int]:
        if not root or not target:
            return []

        parent_track = {}
        self.mark_parents(root, parent_track)

        visited = set()
        queue = deque()
        queue.append((target, 0))  # Tuple: (node, distance from target)
        ans = []

        while queue:
            cur, distance = queue.popleft()
            visited.add(cur.val)

            if distance == k:
                ans.append(cur.val)

            if cur.left and cur.left.val not in visited:
                queue.append((cur.left, distance + 1))
            if cur.right and cur.right.val not in visited:
                queue.append((cur.right, distance + 1))
            if cur.val in parent_track and parent_track[cur.val].val not in visited:
                queue.append((parent_track[cur.val], distance + 1))

        return ans

                