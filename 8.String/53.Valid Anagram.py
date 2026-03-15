# # Intuition
# 輸入的兩個字串，彼此是重新排序後的字串 (nanagram)

# # Approach
# 使用 Counter，注意counter內的字串排序

# # Complexity
# - Time complexity:O(N)
# - Space complexity:O(N)

# language: Python
from collections import Counter # 統計字串中每個字元出現次數
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # if len(s) == len(t) and set(s) == set(t):
        if len(s) == len(t) and Counter(s) == Counter(t):
            return True
        else:
            return False