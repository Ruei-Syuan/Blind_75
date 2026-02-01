# # Intuition
# 給你一個字串 s 和一個字典（字串集合）wordDict，這個字串能不能被「拆分」成一連串字典裡的單字？

# # Approach
# DP

# # Complexity
# - Time complexity:O(n³)
# - Space complexity:O(n)

# language: Python
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordSet = set(wordDict)  # 用 set 加速查詢
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # 空字串可拆分

        for i in range(1, n + 1):
            for j in range(i):
                # 檢查 s[j:i] 是否在字典裡，且前面能拆成功
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break  # 找到一種拆法就可以停了

        return dp[n]
    
        # [FAIL] aaa, aaaa => aaaaaaa => 誤判 F
        # wordDict = list(set(wordDict))
        # sorted_words = sorted(wordDict, key=len)

        # for word in sorted_words:
        #     s  = s.replace(word, "")

        # if len(s) == 0:
        #     return True
        # else:
        #     return False
