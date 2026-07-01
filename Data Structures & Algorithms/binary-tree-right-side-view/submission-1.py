# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        only the first node at each level where right is accessed first
        ans = [1 3]
        current_level   = [5 4] (queue)
        next_level      = [] (queue)


        add root to current level
        
        while (current_level)
            -> node = pop current level
            -> push to new level node.right, node.left
            -> add node to ans

            while (current_level)
                -> node = pop current level
                -> push to new level right, left

            -> current level becomes new level
            -> new level empty
        """

        if not root:
            return []

        ans = list()
        current_level = deque([root])
        new_level = deque()

        while current_level:
            node = current_level.popleft()
            ans.append(node.val)

            if node.right:
                    new_level.append(node.right)
            if node.left:
                    new_level.append(node.left)

            while current_level:
                node = current_level.popleft()
                if node.right:
                    new_level.append(node.right)
                if node.left:
                    new_level.append(node.left)

            current_level = new_level
            new_level = deque()

        return ans
            