"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

Constraints:
The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000
"""
from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
    #DFS Recusrive approach
        # if not root:
        #     return 0
        #
        # # If one child is missing, return depth of the other side
        # if not root.left:
        #     return self.minDepth(root.right) + 1
        # if not root.right:
        #     return self.minDepth(root.left) + 1
        #
        # # Both children exist, take minimum of both depths
        # return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


    # BFS Iterative approach
        if not root :
            return 0

        queue = deque ([(root, 1)])

        while queue:
            node , depth = queue.popleft()

            if not node.left and not node.right:
                return depth

            if node.left:
                queue.append((node.left, depth+1))

            if node.right:
                queue.append((node.right, depth+1))

 # Create tree:     3
    #                /   \
    #               9     20
    #                    /  \
    #                   15   7
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sol = Solution()
print(sol.minDepth(root))