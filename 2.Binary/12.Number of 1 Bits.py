# # Intuition
# Given a positive integer n, returns the number of set bits in its binary representation (also known as the Hamming weight).
# 計算正整數 n 的二進位表示中有多少個1，也就是 Hamming weight

# # Approach
# Brian Kernighan’s Algorithm (定義：一種計算 Hamming weight 的演算法)
# REF: 
# https://170530.medium.com/%E8%A8%88%E7%AE%97-1-%E5%80%8B-word-%E8%A3%A1%E6%9C%89%E5%B9%BE%E5%80%8B-on-%E7%9A%84-bit-00bad633f40d

# # Complexity
# - Time complexity:O(log n)
# - Space complexity:O(log n)

# language: Python
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count("1")
    
print(Solution().hammingWeight(11))   # 輸出 3

# # 方法 1：逐位檢查
# def hammingWeight_shift(n):
#     count = 0
#     while n:
#         count += n & 1
#         n >>= 1
#     return count

# # 方法 2：Brian Kernighan’s Algorithm
# def hammingWeight_kernighan(n):
#     count = 0
#     while n:
#         n &= (n - 1)
#         count += 1
#     return count

# # 方法 3：內建函數
# def hammingWeight_builtin(n):
#     return bin(n).count("1")

# # 測試
# print(hammingWeight_shift(11))      # 3
# print(hammingWeight_kernighan(11))  # 3
# print(hammingWeight_builtin(11))    # 3