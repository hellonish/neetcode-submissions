
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
        if not root: return []

        queue = deque([root])
        traversal = []

        while queue:
            current_level = []
            
            for _ in range(len(queue)):
                node = queue.popleft()
                current_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            traversal.append(current_level)

        return traversal