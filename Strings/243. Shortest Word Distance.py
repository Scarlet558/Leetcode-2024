"""
Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

Example 1:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3
Example 2:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1

Constraints:

2 <= wordsDict.length <= 3 * 104
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
word1 != word2
"""


class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        mindist = float("inf")
        val1 = -1
        val2 = -1

        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                val1 = i
            elif wordsDict[i] == word2:
                val2 = i

            if val1 != -1 and val2 != -1:
                mindist = min(mindist, abs(val1 - val2) )


        return mindist



wordsDict = ["a","a","b","b"]
word1 = "a"
word2 = "b"

print(Solution().shortestDistance(wordsDict, word1, word2))