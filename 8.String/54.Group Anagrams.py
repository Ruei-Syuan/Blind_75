# # Intuition
# 

# # Approach
# 

# # Complexity
# - Time complexity:O(N)
# - Space complexity:O(K)

# language: Python
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # [原先寫法] 效能問題
        # outList = []
        # while len(strs) > 0:
        #     ss = strs[0]
        #     inList = []
        #     inList.append(ss)
        #     strs.pop(0)
        #     strs2 = strs[:]   # ✅ 用切片复制，避免遍历时修改原列表
        #     for s1 in strs2:
        #         if Counter(ss) == Counter(s1):
        #             inList.append(s1)
        #             strs.remove(s1)
        #     outList.append(inList)
        
        # return outList
        from collections import defaultdict
        
        # 建立一个默认字典，key 不存在时自动生成一个空列表
        anagrams = defaultdict(list)

        # 遍历输入的每个字符串
        for s in strs:
            # 将字符串排序后作为 key
            # 例如 "eat" -> "aet", "tea" -> "aet"
            key = ''.join(sorted(s))

            # 把原始字符串加入对应的分组列表
            anagrams[key].append(s)

        # 返回所有分组的列表（字典的值部分）
        return list(anagrams.values())
