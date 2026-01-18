# 打開 VS Code 的 內建終端機（快捷鍵：Ctrl + `） => run code

# Hash（中文常譯為「雜湊」或「雜湊函式」）是一種「將任意長度的輸入資料，透過數學運算壓縮成一段固定長度雜湊值」的函式

# 題目:
# 輸入 - 陣列 & TGT / 輸出 - 哪兩個 index 的數字相加是 TGT

# 解題思路: 
# 1.新增字典拿來儲存目標減掉每個陣列中的數字
# 2.利用 HASH 原理 進行計算

# language: Python3

class Solution:
    def twoSum(self, nums: [], target: int) -> []:
        # use hash, 將兩個數字相減
        seen = {} # build a dictionary
        # print("seen, ", seen)
        for i, value in enumerate(nums):
            # print(i, value)
            gap = target - value # gap 等於 TGT 扣掉 陣列中的數字 (即. val + ? = TGT)
            # print('g:', gap)
            if gap in seen: # 如果字典中有我缺的剩餘 gap
                return (seen[gap], i) # 輸出那個gap所在的index, 以及我自己的index
            
            seen[value] = i # 否則將我自己的值 存入字典
            # print("seen, ", seen)
        
        return None # if no answer

ss = Solution()
nums = [2, 7, 11, 15]
print(ss.twoSum(nums, 9))   # (0, 1)