# # Intuition
# 書入一個旋轉過的陣列 以及 TGT, 輸出 TGT 所在位置需要旋轉幾次

# # Approach
# 解法: 先使用 binary search 找出最小值(中心點) ，再用二分搜尋法找到 TARGET

# # Complexity
# - Time complexity:O(log n)
# - Space complexity:O(1)

# language: Python
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target not in nums:
            return -1
        
        # Step 1: 找旋轉點 (pivot)
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left   # 最小值的位置，也就是旋轉點

        # Step 2: 用二分搜尋找 target
        left, right = 0, len(nums) - 1
        if target >= nums[pivot] and target <= nums[right]:
            left = pivot
        else:
            right = pivot - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    
# 範例測試
print(Solution().search([4,5,6,7,0,1,2],0))  # 輸出: 0