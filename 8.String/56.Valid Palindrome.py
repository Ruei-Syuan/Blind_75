# # Intuition
# 字串是否為 回文

# # Approach
# 字串處理

# # Complexity
# - Time complexity:O(N)
# - Space complexity:O(K)

# language: Python
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 過濾，只留下字母並轉大寫
        s = s.replace(" ", "")

        # 空字串視為 True
        if s == "":
            return True
            
        # s = "".join(ch.upper() for ch in s if ch.isalpha())
        
        # 過濾，只留下字母或數字，並轉小寫
        s = "".join(ch.lower() for ch in s if ch.isalnum())

        return s == s[::-1]

        # if len(s)%2 == 1:
        #     left = s[:(len(s)-1)//2]
        #     right = s[(len(s)-1)//2:]
        
        # else:
        #     left = s[:len(s)/2]
        #     right = s[len(s)/2:]
        
        # rever_right = right[::-1]

        # return left==rever_right


        
        