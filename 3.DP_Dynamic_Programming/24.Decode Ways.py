# # Intuition
# 編碼 1~26, 請問輸入字串可以有幾種解碼方式?

# # Approach
# DP，每一步的答案 = 「能單獨解碼，加上前一步的解法」 + 「能兩個字一起解碼，加上前兩步解法」

# # Complexity
# - Time complexity:O(n)
# - Space complexity:O(n)

# language: Python
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == "0":
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        # dp[len(s)] = 0*len(s)
        dp[0] = 1  # 空字串
        dp[1] = 1  # 第一個字元不是 0

        for i in range(2, n + 1):
            # 單字元能解碼
            # - 我們在算 dp[i] 的時候，對應的字元是 s[i-1]
            # - dp[1] → 前 1 個字元 "2" → 對應 s[0]
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            # 雙字元能解碼 (10~26)
            if "10" <= s[i-2:i] <= "26":
                dp[i] += dp[i-2]
        
        return dp[-1]