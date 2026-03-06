# # Intuition
# 從 index = 0 開始走，每走一步，下一步必須走現在的值的步數，判斷最遠可否走到最後一個元素

# # Approach
# - Greedy = 當下最佳選擇，不回頭
# 一層迴圈，使用最遠距離
# - [2,3,1,1,4]
# - 從 0 開始，能跳到最遠位置是 2。
# - 到 index 1 時，能跳到最遠位置是 4。
# - 4 ≥ 最後一格 → 成功。
# - [3,2,1,0,4]
# - 到 index 3 時，nums[3] = 0，最遠只能到 3。
# - 但最後一格在 4 → 卡住

# # Complexity
# - Time complexity:O(n)
# - Space complexity:O(n)

# language: Python
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxReach = 0  # 目前能到的最遠位置
        for i, jump in enumerate(nums):
            # 如果當前位置超過最遠能到的位置 → 卡住
            if i > maxReach:
                return False
            # 更新最遠能到的位置
            maxReach = max(maxReach, i + jump)
        return True
