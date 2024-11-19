"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [4,6,7,5,2,9,8,3,1]


Example 3:
Input: root = []
Output: []

Example 4:
Input: root = [1]
Output: [1]


Constraints:
The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []

        stack = []
        res = []
        cur = root
        last_visited = None

        while cur or stack :
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack[-1]

            if cur.right and cur.right != last_visited:
                cur = cur.right
            else:
                res.append(cur.val)
                last_visited = stack.pop()
                cur = None

        return res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(7)
root.right.right.left = TreeNode(9)

sol = Solution()
print(sol.postorderTraversal(root))

