# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        ans = defaultdict(list)
        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()
            if depth % 2 == 0: ans[depth].append(node.val)
            else: ans[depth].insert(0, node.val)
            if node.left: queue.append((node.left, depth+1))
            if node.right: queue.append((node.right, depth+1))
        return ans.values()