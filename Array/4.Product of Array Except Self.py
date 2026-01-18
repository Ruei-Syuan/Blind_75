# # Intuition
# 輸入陣列 // 如果陣列中元素都屬於唯一則輸出true, else false

# # Approach
#  將list轉成set後的長度做比較

# # Complexity
# - Time complexity:O(n)
# - Space complexity:O(n)

# language: Python
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1] * n
        print(res)

        # 前綴乘積
        prefix = 1
        for i in range(n):
            print('res', res[i])
            res[i] = prefix
            print('res', res[i])
            prefix *= nums[i]
            print('prefix', prefix)

        # 後綴乘積
        suffix = 1
        for i in range(n-1, -1, -1):
            print('res', res[i])
            res[i] *= suffix
            print('res', res[i])
            suffix *= nums[i]
            print('suffix', prefix)

        return res
    
nums = [1, 2, 3, 4]
print(Solution().productExceptSelf(nums))
# 輸出: [24, 12, 8, 6]