# # Intuition
# 輸入一個陣列，理論上是從 0-n，輸出少了的人

# # Approach
# (1)位元運算 (2)字串反轉法<效能差 需要space:O(32)>
# - 第一次：取最低位 1 → result = 1
# - 第二次：取最低位 0 → result = 10 (二進位)
# - 第三次：取最低位 1 → result = 101

# # Complexity
# - Time complexity:O(32)
# - Space complexity:O(1)

# language: Python
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for i in range(32):
            # 取出最低位
            bit = n & 1
            # 左移結果，並加上 bit
            result = (result << 1) | bit
            # 原數字右移
            n >>= 1
        return result