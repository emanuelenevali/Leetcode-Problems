class Solution(object):
    @classmethod
    def lengthOfLongestSubstring(cls, s):
        """
        :type s: str
        :rtype: int
        """
#         pos = []
#         row = 0
#         for c in s:
#             #print([ind for ind, char in enumerate(s) if char == c])
#             pos.append([ind for ind, char in enumerate(s) if char == c])
#             row += 1
#         #print(pos)
        best_len=0
        best_string=""
        for i in range(len(s)):
           #print(s[i])
           current_string = s[i]
           current_len=1
           list_of_chars=[s[i]]
           for j in range(i+1, len(s)):
               #print(s[j])
               #print("list of chars: ", list_of_chars)
               if s[j] not in list_of_chars:
                   current_len +=1
                   current_string = current_string+s[j]
                   list_of_chars.append(s[j])
               else:
                   #print("brekkato")
                   break
               #print(current_string)
           print(current_len)
           print("all iterazioine {} la lunghezza della stringa migliore è {}".format(i, best_len))
           if current_len>best_len:
               best_string = current_string
               best_len = current_len
               print(best_string)
           #print("----------------------------------------------------------")
        return best_len

            



              

s = "abcabcbb"
print(Solution.lengthOfLongestSubstring(s))

