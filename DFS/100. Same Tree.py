"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Input: p = [1,2,3], q = [1,2,3]
Output: true

Input: p = [1,2], q = [1,null,2]
Output: false

Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
"""
from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        # # Base cases
        # if not p and not q: # Both empty
        #     return True
        # if not p or not q:# One empty, one not
        #     return False
        #
        # # Check current nodes and recursively check subtrees
        # return ( p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))

        #BFS

        queue = deque ([(p,q)])

        while queue:
            node1, node2 = queue.popleft()


            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False

            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))





