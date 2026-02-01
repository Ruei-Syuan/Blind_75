# # Intuition
# 輸入兩個字串, 找出兩字串中「共同的子序列」長度  # Longest Common Subsequence (LCS)
# Input: text1 = "abcde", text2 = "ace" # Output: 3  

# # Approach
# DP拆解
# - 字母相同 → 往左上角看，加 1。
# - 字母不同 → 往上或往左看，取最大值。

# # Complexity
# - Time complexity:O(m*n)
# - Space complexity:O(m*n)

# language: Python
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m, n = len(text1), len(text2)
        # 建立 DP 表格
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 填表
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # 回溯找出子序列
        # i, j = m, n
        # lcs_str = []
        # while i > 0 and j > 0:
        #     if text1[i - 1] == text2[j - 1]:
        #         lcs_str.append(text1[i - 1])
        #         i -= 1
        #         j -= 1
        #     elif dp[i - 1][j] >= dp[i][j - 1]:
        #         i -= 1
        #     else:
        #         j -= 1

        return dp[m][n] #, ''.join(reversed(lcs_str))