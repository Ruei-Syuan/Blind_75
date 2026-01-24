# # Intuition
# Given an integer array nums, Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# 給一個陣列，輸出任兩個最大的面積

# # Approach
# 解法: 雙指針法：高效，時間複雜度 O(n)。
# 陷阱: - 移動較短的那一邊的指針，因為高度受限於短邊，移動長邊不會增加面積。

# # Complexity
# - Time complexity:O(n)
# - Space complexity:O(1)

# language: Python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1
        max_contain = 0
        while l < r:
            h, w = min(height[l], height[r]), (r-l)
            contain = h * w
            max_contain = max(contain, max_contain)
            # 移動短邊就好
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        
        return max_contain
    
# 範例測試
print(Solution().maxArea([1,8,6,2,5,4,8,3,7])) # 輸出 49