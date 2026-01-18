# # Intuition
# <!-- Describe your first thoughts on how to solve this problem. -->
# 輸入陣列 // 如果陣列中元素都屬於唯一則輸出true, else false

# # Approach
# <!-- Describe your approach to solving the problem. -->
#  將list轉成set後的長度做比較

# # Complexity
# - Time complexity:O(n)
# - Space complexity:O(n)

# language: Python3
class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        distinct_nums = set(nums)
        return not len(nums) == len(distinct_nums)
    
ss = Solution()
input = [1,1,1,3,3,4,3,2,4,2]
print(ss.containsDuplicate(input))