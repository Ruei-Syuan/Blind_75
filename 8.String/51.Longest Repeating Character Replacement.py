# # Intuition
# - 輸出最長"重複的"子字串"長度" & 給予你k次機會將中間不一樣的字母掉包成任意字元

# # Approach
# 字典 + 滑動視窗

# # Complexity
# - Time complexity:O(N)
# - Space complexity:O(K)

# language: Python
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # 用字典計數，維護 max_count，並用公式 (視窗長度 - max_count) <= k 判斷是否需要縮小視窗。
        count = {}
        left = 0
        max_count = 0
        answer = 0

        for right in range(len(s)):
            # - count 是一個字典，用來記錄每個字元在目前視窗中的出現次數。
            # - count.get(s[right], 0)：如果字元 s[right] 已經在字典裡，就取它的值；如果沒有，就回傳 0。
            # - max_count 用來記錄目前視窗中「出現次數最多的字元」的次數。
            count[s[right]] = count.get(s[right], 0) + 1
            max_count = max(max_count, count[s[right]])

            # 如果需要替換的字元數超過 k，就縮小視窗
            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1

            answer = max(answer, right - left + 1)

        return answer
