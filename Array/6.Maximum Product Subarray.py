# # Intuition
# Given an integer array nums, find a subarray that has the largest product, and return the product.

# # Approach
# 解法: (1)Kadane Algorithm (2)DP <最左/最右/中間 遞迴>
# 陷阱: 「最大乘積子陣列」需同時追蹤 最大值 和 最小值，因為負數可能會翻轉結果

# # Complexity
# - Time complexity:O(n)
# - Space complexity:O(1)

# language: Python
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = len(nums)
        cur_max = nums[0]
        cur_min = nums[0]
        result = nums[0]

        for num in nums[1:]:
            temp_max = max(num, cur_max * num, cur_min * num)
            cur_min = min(num, cur_max * num, cur_min * num)
            cur_max = temp_max
            result = max(result, cur_max)

        return result