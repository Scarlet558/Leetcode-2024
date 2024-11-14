"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.

"""
import collections


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
    # ransomNote = "aa", magazine = "aab"

        mag_map = collections.Counter(magazine)

        for chr in ransomNote:
            if chr not in mag_map:
                return False
            else:
                mag_map[chr] -= 1

            if mag_map[chr] == 0:
                del mag_map[chr]

        return True

sol = Solution()
print(sol.canConstruct("a", "b"))