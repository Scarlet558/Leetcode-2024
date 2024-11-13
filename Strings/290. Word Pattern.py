"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.


Example 1:

Input: pattern = "abba", s = "dog cat cat dog"

Output: true

Explanation:

The bijection can be established as:

'a' maps to "dog".
'b' maps to "cat".
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"

Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"

Output: false



Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.

"""
"""
Key Insight: Need to establish a two-way (bijective) mapping between pattern characters and words
Main Steps:

Split string into words
Check if pattern length matches words length
Use two dictionaries to maintain both mappings:

pattern char → word
word → pattern char

Check each char-word pair for consistency

Edge Cases:

Different lengths between pattern and words
Same char mapping to different words
Same word mapping to different chars

"""

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        word = s.split()

        pattern_word_map = {}
        word_pattern_map = {}

        if len(word) != len(pattern):
            return False

        for word, pattern in zip(word, pattern):
            if pattern in pattern_word_map:
                if pattern_word_map[pattern] != word:
                    return False
            elif word in word_pattern_map:
                if word_pattern_map[word] != pattern:
                    return False
            else:
                pattern_word_map[pattern] = word
                word_pattern_map[word] = pattern
        return True




pattern = "abba"
s = "dog cat cat dog"
solution = Solution()
print(solution.wordPattern(pattern, s))

