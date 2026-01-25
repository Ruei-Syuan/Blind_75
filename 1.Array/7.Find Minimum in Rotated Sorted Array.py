# # Intuition
# 正確的陣列會是由小到大排序，題目輸入一個被旋轉過的陣列，你必須根據算出來的旋轉次數，來取得正確陣列的切片中的最小值作為輸出

# 📌 2. 常見演算法複雜度
# - O(\log n)：二分搜尋 (Binary Search)、平衡樹查找。
# - O(n\log n)：快速排序 (Quick Sort)、合併排序 (Merge Sort)、堆排序 (Heap Sort)

# - \log n：就像「每次把問題砍一半」，所以成長很慢。
# - n\log n：就像「每個元素都要處理，但每次處理還要花 \log n 的時間」，所以比線性更大

# # Approach
# 解法: (1)Binary Search : 原理 設定左右邊界, 每次拿中間的值去做比對

# # Complexity
# - Time complexity:O(log n)
# - Space complexity:O(1)
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # 如果中間值比右邊大，最小值一定在右半邊
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # 否則最小值在左半邊（包含 mid）
                right = mid
        
        return nums[left]

# 🔎 你的程式碼問題
# sorted(nums) → 排序整個陣列，時間複雜度 O(n\log n)。
# 找最小值的方式是透過比對排序後的結果，這違背了題目要求的效率。
# 邏輯: 先將陣列排序，如果輪迴一圈 等於陣列長度，其餘則透過迴圈找到旋轉次數，最後取得切片最小值
# - Time complexity:O(n log n)
# - Space complexity:O(1)
# class Solution(object):
#     def findMin(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         r_times = 0
#         sorted_nums = sorted(nums)
        
#         if sorted_nums[0] == nums[0]:
#             r_times = len(nums)
#         else:
#             for i, value in enumerate(nums):
#                 if value == sorted_nums[0]:
#                     r_times = i

#         return min(sorted_nums[0:r_times+1])

# 範例測試
print(Solution().findMin([4,5,6,7,0,1,2]))  # 輸出: 0