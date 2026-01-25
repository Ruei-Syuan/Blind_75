# # Intuition
# 輸入一串陣列 // 輸出一樣長度，其中每個元素為 排除自己之外的元素相乘乘績

# # Approach
# 迷思: 先算出整個陣列的相乘結果，依序將結果除上自己即可 -> 遇到元素 0 會產生 ZeroDivisionError
# 解法: 利用前綴乘積 + 後綴乘積，答案 = 前綴 × 後綴。

# # Complexity
# - Time complexity:O(n)
# - Space complexity:O(1)

# language: Python

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1] * n # 建立空 list

        # 前綴乘積
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
            
        # 後綴乘積
        suffix = 1
        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
            
        return res
    
nums = [1, 2, 3, 4]
print(Solution().productExceptSelf(nums))
# 輸出: [24, 12, 8, 6]