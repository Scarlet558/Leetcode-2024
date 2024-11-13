"""
You are playing a Flip Game with your friend.

You are given a string currentState that contains only '+' and '-'. You and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move, and therefore the other person will be the winner.

Return all possible states of the string currentState after one valid move. You may return the answer in any order. If there is no valid move, return an empty list [].


Example 1:

Input: currentState = "++++"

Possible moves:
1. Flip first two '++'  : "--++"
2. Flip middle two '++'  : "+--+"
3. Flip last two '++'   : "++--"

Output: ["--++", "+--+", "++--"]


Example 2:
Input: currentState = "+"
Output: []


Constraints:

1 <= currentState.length <= 500
currentState[i] is either '+' or '-'.
"""
"""
Key Insight:

Find pairs of '++' and convert to '--' keeping rest of string same

Core Steps:

Loop through string checking pairs
If '++' found: create new string with '--' at that position
Add to result list

"""


class Solution(object):
    def generatePossibleNextMoves(self, currentState):
        """
        :type currentState: str
        :rtype: List[str]
        """

        res = []

        for i in range(len(currentState)-1):
            if currentState[i:i+2] == "++":
                new_state = currentState[:i] + '--' + currentState[i+2:]
                res.append(new_state)

        return res

s = Solution()
print(s.generatePossibleNextMoves("++++"))
