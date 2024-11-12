'''

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        barcket_map = {
            ']' : '[',
            '}' : '{',
            ')' : '(',
        }

        stack = []

        for char in s:
            if char in barcket_map:
                if stack:
                    top_ele = stack.pop()
                else :
                    top_ele = 'X'

                if top_ele != barcket_map[char]:
                    return False
            else :
                stack.append(char)
        return not stack


print(Solution().isValid("()"))
print(Solution().isValid("()[]{}"))
print(Solution().isValid("(]"))
