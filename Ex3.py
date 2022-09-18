# class Solution(object):
#     @classmethod
#     def lengthOfLongestSubstring(cls, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         pos = []
#         row = 0
#         for c in s:
#             #print([ind for ind, char in enumerate(s) if char == c])
#             pos.append([ind for ind, char in enumerate(s) if char == c])
#             row += 1
#         #print(pos)


#class Solution(object):
#    def lengthOfLongestSubstring(self, s):
#        """
#        :type s: str
#        :rtype: int
#        """
#        for c in s:



              

s = "abcaabcdefghjaba"
l = list(s)
# Solution.lengthOfLongestSubstring(s)
print(s,l)
