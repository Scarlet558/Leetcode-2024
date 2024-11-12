def gcdOfStrings(self, str1, str2):
    """
    :type str1: str
    :type str2: str
    :rtype: str
    """
    if str1 + str2 != str2 + str1:
        return ""

    if len(str1) == len(str2):
        return str1

    if (len(str1) > len(str2)):
        return self.gcdOfStrings(str1[len(str2):], str2)
    return self.gcdOfStrings(str1, str2[len(str1):])


'''
Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
'''