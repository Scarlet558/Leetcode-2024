"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:

Input: s = "foo", t = "bar"

Output: false

Explanation:

The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:

Input: s = "paper", t = "title"

Output: true

"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s1_map =  {}
        s2_map = {}

        for s_1, s_2 in zip(s, t): #  iterates over two sequences, s and t, in paralle
            print(s_1,s_2)
            if (s_1 not in s1_map ) and (s_2 not in s2_map):
                s1_map[s_1] = s_2
                s2_map[s_2] = s_1
            else :
                if s1_map.get(s_1)  != s_2 or s2_map.get(s_2) != s_1 :
                    return False
        return True

s = "badc"
t = "baba"
print(Solution().isIsomorphic(s, t))