class Solution:
    def lowestCommonAncestor(
        self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
    ) -> 'TreeNode':
        """
        Find the lowest common ancestor (LCA) of two nodes in a binary tree.
      
        Args:
            root: The root node of the binary tree
            p: First target node
            q: Second target node
          
        Returns:
            The lowest common ancestor node of p and q
        """
        if root in (None, p, q):
            return root
      
        left_result = self.lowestCommonAncestor(root.left, p, q)
      
        right_result = self.lowestCommonAncestor(root.right, p, q)
      
        if left_result and right_result:
            return root
      
        return left_result or right_result