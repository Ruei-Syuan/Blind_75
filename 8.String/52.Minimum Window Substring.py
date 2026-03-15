# # Intuition
# - 輸入：字串 s 與字串 t
# - 輸出：s 中最短的子字串，必須包含 t 的所有字元（含重複次數）。
# - 若不存在：回傳空字串 ""。

# # Approach
# - 建立需求表：用 Counter(t) 記錄 t 中每個字元的需求數量。
# - 滑動窗口：用兩個指標 left、right 控制當前窗口。
# - 擴展右邊：不斷加入字元，直到窗口滿足需求。
# - 收縮左邊：嘗試縮小窗口，確保仍滿足需求。
# - 更新答案：在每次滿足需求時，檢查是否比目前最短更短

# # Complexity
# - Time complexity:O(N)
# - Space complexity:O(K)

# language: Python

from collections import Counter # 統計字串中每個字元出現次數

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""   # 如果有空字串，直接回傳空結果
        
        need = Counter(t)   # 記錄 t 中每個字元需要的數量
        window = {}         # 窗口中目前的字元計數
        have, need_count = 0, len(need)  # have: 已滿足的字元種類數, need_count: 總共需要的字元種類數
        
        res, res_len = [-1, -1], float("inf")  # res: 最佳窗口的左右邊界, res_len: 最短長度
        left = 0   # 左指標初始化
        
        # 右指標開始遍歷字串 s
        for right, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1  # 將字元加入窗口計數
            
            # 如果這個字元在需求表中，且數量剛好達到需求
            if ch in need and window[ch] == need[ch]:
                have += 1
            
            # 當窗口已經滿足所有需求字元
            while have == need_count:
                # 更新最短窗口
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                
                # 收縮左邊，嘗試縮小窗口
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1  # 如果縮掉後不再滿足需求，更新 have
                left += 1
        
        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""
