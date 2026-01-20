# # Intuition
# 輸入一個陣列，輸出所有三個元素相加為0的數字

# # Approach
# 解法: 先將一個參數固定，透過雙指標的挪動，進行組合 n^3 --> n^2

# # Complexity
# - Time complexity:O(n^2)
# - Space complexity:O(1)

# language: Python
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        for i in nums:
            res = []
            nums.sort()
            n = len(nums)

            for i in range(n - 2):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue  # 避免重複解

                left, right = i + 1, n - 1
                while left < right:
                    total = nums[i] + nums[left] + nums[right]

                    if total == 0:
                        res.append([nums[i], nums[left], nums[right]])
                        # 跳過重複值
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < 0:
                        left += 1
                    else:
                        right -= 1
            return res
