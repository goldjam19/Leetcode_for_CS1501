#Write a function to find the longest common prefix string amongst an array of strings
#If there is no common prefix, return an empty string ""

class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = ''
        if strs == []:
            return prefix
        if len(strs) == 1:
            return strs[0]
        strs.sort()
        shortest = strs[0]
        for i in range(len(shortest)):
            if strs[len(strs) - 1][i] == shortest[i]:
                prefix += strs[len(strs) - 1][i]
            else:
                break
        return prefix
        