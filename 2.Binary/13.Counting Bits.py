# # Intuition
# Given an integer n, 回傳從0開始到n-1中每個數字的 Hamming weight
# 又稱為: bit DP

# # Approach
# 延續上一題, 用迴圈搭配字串做運算
# 小學生解釋法:「一個數字的 1 的數量 = 去掉最後一位的數字的 1 的數量 + 最後一位是不是 1」

# # Complexity
# - Time complexity:O(n)
# - Space complexity:O(n)

# language: Python
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # [法一] 效能上稍慢，因為每次都要轉字串再數字
        # Time complexity: O(n log n)
        # Space complexity: O(log n) 
        # arr = []
        # for i in range(n+1):
        #     arr.append(bin(i).count("1"))

        # [法二] 動態規劃 + 位運算 (使用 BIT 運算)
        # 二進位的結構分解：
            # 去掉最後一位 → 前半段的 bit count
            # 最後一位 → 用 & 1 判斷
        # - Time complexity:O(n)
        # - Space complexity:O(n)
        arr = [0] * (n + 1)
        for i in range(1, n + 1):
            arr[i] = arr[i >> 1] + (i & 1)

        return arr        
        
     
print(Solution().countBits(2))   # 輸出 [0,1,1]