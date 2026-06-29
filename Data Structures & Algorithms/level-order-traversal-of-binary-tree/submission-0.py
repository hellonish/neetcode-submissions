# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        traversal = []
        queue = []

        curr_level = [1] 
        new_level = [2 3]

        if queue empty:
            queue = new_level
            traversal = curr_level

        """
        if not root:
            return []

        traversal = []

        queue = deque()
        queue.append(root)

        current_level = []
        new_level = []
        while queue:
            node = queue.popleft()

            current_level.append(node.val)
            if node.left:
                new_level.append(node.left)
            if node.right:
                new_level.append(node.right)

            if not queue:
                traversal.append(current_level)
                
                if new_level: # when new_level is not empty
                    queue.extend(new_level)

                current_level = []
                new_level = []

        return traversal
