# # Intuition
# 

# # Approach
# dict 判斷

# # Complexity
# - Time complexity:O(N)
# - Space complexity:O(K)

# language: Python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = list(s)
        if len(s)%2 > 0: # 奇數長度一定不可能完全匹配
            return False
        
        brackets = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        tmp = []
        for ss in s:
            # print('SS:', ss, 'tmp:', tmp)
            if len(tmp)>0 and tmp[-1] in brackets and brackets[tmp[-1]] == ss:
                tmp.pop()
            else:
                tmp.append(ss)
            # print('/ss:', ss, 'tmp:', tmp)
        
        return len(tmp) == 0

ss = Solution()
# print(ss.isValid("({[)"))
