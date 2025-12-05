from collections import deque
from typing import Optional, List

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Returns the values of nodes visible from the right side of a binary tree.
      
        Uses BFS (level-order traversal) to process nodes level by level,
        capturing the rightmost node at each level.
      
        Args:
            root: The root node of the binary tree
          
        Returns:
            List of integers representing the right side view of the tree
        """
        result = []
      
        # Handle empty tree case
        if root is None:
            return result
      
        # Initialize queue with root node for BFS
        queue = deque([root])
      
        # Process tree level by level
        while queue:
            level_size = len(queue)
          
            # Process all nodes at current level
            for i in range(level_size):
                current_node = queue.popleft()
              
                # Add the rightmost node of this level to result
                # (This happens when i == level_size - 1)
                if i == level_size - 1:
                    result.append(current_node.val)
              
                # Add children to queue for next level processing
                # Add left child first, then right child
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
      
        return result