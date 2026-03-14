# # Intuition
# - 輸出最長"不重複的"子字串"長度"

# # Approach
# 雙指標 + HashSet

# # Complexity
# - Time complexity:O(N)
# - Space complexity:O(K)

# language: Python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # [法一] 暴力拆解字串，SET會打亂順序回傳
        # def find_max_subseq(ss):
        #     return ''.join(set(list(ss)))  # 找出最大 subsequence (字元)

        # all_max_string = find_max_subseq(s)
        # all_max_string_len = len(all_max_string)

        # answer = 0
        # # 判斷迴圈中有誰 
        # for i in range(len(s)):
        #     sub_str = s[i:i+all_max_string_len]
        #     no_dup_substr = find_max_subseq(sub_str)
            # if len(sub_str) == len(no_dup_substr):
            #     return len(no_dup_substr)
            
        #     if len(no_dup_substr) > answer:
        #         answer = len(no_dup_substr)

        # return answer

        # 雙指標 + HashSet
        seen = set()
        left = 0
        answer = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            answer = max(answer, right - left + 1)

        return answer