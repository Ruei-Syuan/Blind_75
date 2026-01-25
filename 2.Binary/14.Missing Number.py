# # Intuition
# 輸入一個陣列，理論上是從 0-n，輸出少了的人

# # Approach
# 

# # Complexity
# - Time complexity:O(log n)
# - Space complexity:O(log n)

# language: Python
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [法1] 總和公式 n*(n+1)//2 扣掉現在陣列加總
        n = len(nums)
        return n*(n+1)//2 - sum(nums)

        # [法2] 利用 XOR 的特性：相同數字 XOR 會抵消
        # [補充] XOR 的特性
            # 相同數字 XOR 會抵消，例如：a ^ a = 0
            # 任何數字和 0 XOR 還是自己，例如：a ^ 0 = a
            # XOR 運算具交換律和結合律，順序不影響結果：a ^ b ^ c = c ^ a ^ b
        # n = len(nums)
        # xor_all = 0
        # for i in range(n+1):
        #     xor_all ^= i
        # for num in nums:
        #     xor_all ^= num
        # return xor_all

        # [法3] 排序法
        # 如果少掉的是最後一個字元 要另外判斷
        # if max(nums) != len(nums):
        #     return len(nums)        
        # nums.sort() # 將輸入做排序
        # # only 少掉非最後一個字元，才跑回圈篩選
        # for i, val in enumerate(nums):
        #     if i != val:
        #         return i

        