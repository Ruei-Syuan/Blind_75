# -- =============== 考古題 ==============
# -- 網路
# -- cardinality sorting
# -- linklist
# -- maimum distinct
# -- -- 考過
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