# -- =============== 考古題 ==============
# -- 網路
# -- cardinality sorting
# -- linklist
# -- Maximum num distinct
# -- 考過
# -- alternating prime sequence
# -- slanted cipher
# -- zig zag move
# -- star and bear
# -- =====================================
# -- Cardinality Sorting 的重點是 依照元素出現的次數（頻率）來排序，而不是依照元素本身的大小。
# -- 常見的規則是：
# -- - 先計算每個元素的出現次數。
# -- - 依照頻率排序（可以是由少到多，或由多到少）。
# -- - 如果頻率相同，再用元素值作為次要排序依據。

# ====================== cardinality sorting ==========================
# sorted() 的 key 參數可以回傳一個值，這個值決定排序依據。
# 如果我們回傳一個 tuple，Python 會依序比較 tuple 裡的元素：
# - 先比較第一個元素
# - 如果第一個元素相同，再比較第二個元素
# - 如果第二個元素也相同，再比較第三個元素，以此類推

from collections import Counter

def cardinality_sort(arr):
    freq = Counter(arr) # -- # Step 1: 用 Counter 計算頻率
    # 先依照頻率，再依照數值
    return sorted(arr, key=lambda x: (freq[x], x))

arr = [4, 6, 4, 3, 6, 4, 3]
print(cardinality_sort(arr))
# ================================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        new_node = Node(data)
        if head is None:
            return new_node
        else:
            current = head
            while current.next:
                current = current.next
            current.next = new_node
            return head

# 主程式
mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)

mylist.display(head)

# ====================== 3397. Maximum Number of Distinct Elements After Operations ========================
# 設一個指標 current，表示目前能分配的最小未使用值。
# 對於每個元素 num：
# 它能分配的最小值是 num - k
# 如果 current < num - k，就把它分配到 num - k
# 否則，就把它分配到 current（但不能超過 num + k）
# 每次分配後，current += 1，表示下一個元素要找新的位置
def maxDistinctElements(nums, k):
    nums.sort()
    next_free = float('-inf')
    distinct = 0
    
    for x in nums:
        # 如果 next_free < x - k，直接放到 x - k
        if next_free < x - k:
            next_free = x - k
        # 如果 next_free 在範圍內，就放置
        if next_free <= x + k:
            distinct += 1
            next_free += 1
        # 否則跳過
    
    return distinct

# ================================= alternating prime sequence =============================
# **「Alternating Prime Sequence」通常指的是交錯排列質數的級數，例如：2-3+5-7+11-13+17-...。
# 這個序列的部分和有趣地會在某些位置剛好等於 2 的冪次方，例如 2-3+5=4=2^2，2-3+5-7+11=8=2^3。
# 目前已知能得到的最大冪次是 512=2^9，但是否存在無限多個這樣的情況仍是未解的猜想。
# 「Alternating Prime Sequence」是一個數論趣題，結合了質數分布與交錯級數的特性。它的部分和偶爾會落在 2 的冪次方，但目前數學界沒有完整的證明或解釋，只能依靠電腦驗算與猜想。
# https://math.stackexchange.com/questions/2652169/alternating-series-of-primes
def is_prime(n):
    """判斷 n 是否為質數"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def generate_primes(n):
    """生成前 n 個質數"""
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def alternating_prime_sequence(n):
    """計算交錯質數序列前 n 項部分和"""
    primes = generate_primes(n)
    total = 0
    sequence = []
    for i, p in enumerate(primes):
        if i % 2 == 0:   # 偶數索引 → 加
            total += p
        else:            # 奇數索引 → 減
            total -= p
        sequence.append(total)
    return sequence

def check_powers_of_two(sequence):
    """檢查部分和是否等於 2 的冪次方"""
    results = []
    for i, val in enumerate(sequence, start=1):
        if val > 0 and (val & (val - 1)) == 0:  # 判斷是否為 2 的冪
            results.append((i, val))
    return results

# 測試：前 30 項
seq = alternating_prime_sequence(30)
print("部分和序列:", seq)
print("等於 2 的冪次方的情況:", check_powers_of_two(seq))

# ================================ slanted cipher ================================
# 「Slanted Cipher」是一種簡單的文字加密方法，通常用來把訊息寫成斜向排列，再依照某種規則讀出。它的基本概念是：
# - 把文字寫成矩陣：將明文依序填入一個矩形或方形的字元陣列。
# - 斜向讀取：不是直行或橫行讀，而是沿著斜線（斜向）讀取字元。
# - 得到密文：依照斜向讀取的順序，組合成新的字串。

def slanted_cipher(text, rows):
    # 把文字分成多行
    matrix = []
    for i in range(0, len(text), rows):
        matrix.append(list(text[i:i+rows]))
    
    # 斜向讀取
    result = []
    max_len = max(len(row) for row in matrix)
    for diag in range(rows + max_len - 1):
        for r in range(rows):
            c = diag - r
            if 0 <= c < len(matrix[r]):
                result.append(matrix[r][c])
    return "".join(result)

# 測試
plaintext = "HELLOWORLD"
cipher = slanted_cipher(plaintext, 3)
print("明文:", plaintext)
print("密文:", cipher)

# ===================================================================
# 2075. Decode the Slanted Ciphertext
# 根據輸入字串與寬度，把字串切割成二維list，最後輸出原文
class Solution(object):
    def decodeCiphertext(self, encodedText, rows):
        """
        :type encodedText: str
        :type rows: int
        :rtype: str
        """
        if len(encodedText)==0:
            return ""
        if rows == 1:
            return encodedText
        width = len(encodedText)//rows
        s_list = [list(encodedText[i:i+width]) for i in range(0, len(encodedText), width)]
        res = []
        # 從每一列的起始點開始，沿斜線讀取
        for start_col in range(width):
            r, c = 0, start_col
            while r < rows and c < width:
                res.append(s_list[r][c])
                r += 1
                c += 1

        return "".join(res).rstrip()
        

# ================================ zig zag move ================================
# 是一種 沿斜線或之字形的遍歷方式。你剛剛的 decodeCiphertext 就是典型的「斜線走法」，其實可以視為一種 zig-zag
# - Z 字形排列 (Zig-zag conversion)
class Solution(object):
    def zigzagTraversal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        # 題目必須:
        # 第 0 列（偶數列）從左到右。
        # 第 1 列（奇數列）從右到左。
        # 第 2 列再從左到右。
        ans = []
        skip = True
        for i, row in enumerate(grid):
            if i % 2 == 1: 
                row = row[::-1]
            for x in row:
                if skip:
                    ans.append(x)
                skip = not skip
        return ans
# ================================ star and bear ================================


# class Solution(object):
#     def platesBetweenCandles(self, s, queries):
#         """
#         :type s: str
#         :type queries: List[List[int]]
#         :rtype: List[int]
#         """
#         ans = []
#         for q in queries:
#             # 先擷取字元
#             s2 = s[q[0]:q[1]+1]

#             # 取出 | index
#             start = s2.find('|')      # 第一次出現
#             end = s2.rfind('|')      # 最後一次出現

#             if start==-1 or end==-1 or start==end:
#                 ans.append(0) #沒有符合的candidate
#             else:
#                 s2 = s2[start:end+1].replace('|','')
#                 ans.append(len(s2))
#                 # ans.append(end-start+1-2) #還要扣掉棍子本身
        
#         return ans

class Solution(object):
    def platesBetweenCandles(self, s, queries):
        n = len(s)
        prefixStars = [0] * (n+1)
        nearestLeftBar = [-1] * n
        nearestRightBar = [-1] * n

        # prefix sum of stars
        for i in range(n):
            prefixStars[i+1] = prefixStars[i] + (1 if s[i] == '*' else 0)

        # nearest left bar
        lastBar = -1
        for i in range(n):
            if s[i] == '|':
                lastBar = i
            nearestLeftBar[i] = lastBar

        # nearest right bar
        lastBar = -1
        for i in range(n-1, -1, -1):
            if s[i] == '|':
                lastBar = i
            nearestRightBar[i] = lastBar

        ans = []
        for l, r in queries:
            # l -= 1  # convert to 0-based
            # r -= 1
            leftBar = nearestRightBar[l]
            rightBar = nearestLeftBar[r]
            if leftBar != -1 and rightBar != -1 and leftBar < rightBar:
                ans.append(prefixStars[rightBar] - prefixStars[leftBar])
            else:
                ans.append(0)
        return ans
        ;