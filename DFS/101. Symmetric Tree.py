"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Input: root = [1,2,2,3,4,4,3]
Output: true

Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
"""
from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True

        queue = deque([(root.left,root.right)])

        while queue:
            t1, t2 = queue.popleft()

            if not t1 and not t2:
                continue
            if not t1 or not t2 or t1.val != t2.val:
                return False

            queue.append([t1.left,t2.right])
            queue.append([t1.right,t2.left])

        return True

    #recursion
    """
     def isMirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val) and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
    
    return isMirror(root, root)
    """

# Example 1: Symmetric tree
#      1
#     / \
#    2   2
#   / \ / \
#  3  4 4  3

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

s = Solution()
print(s.isSymmetric(root))