# ======================== 好用語法 ========================
print('*',end='') #輸出後面不要換行, default:\n換行

# 字母小寫
str.lower()
# 計算含有幾個子字串
str.count("str2")

# sort系列(下方有細節)
s = input()
op = s.split()
op_dict = {int(op_str): xfer(op_str) for op_str in op}
# sorted(op_dict.items()) # 按照key排序
# lambda x:x[i] x代表tuple第i個元素 做排序
a = dict(sorted(op_dict.items(), key=lambda item:item[1])) # 按照value小到大排序, 務必要將tuple轉回list

# ===================== map ===========================
map(function, iterable) # list批次處理工具
numbers = [1, 2, 3, 4]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # 輸出：[1, 4, 9, 16]

# ===================== input 格式 ====================
input_lis1 = input()
input_lis1 = input_lis1.split()
l1 = [int(item) for item in input_lis1]

k = list(map(int, input().split())) # 輸入一串數字

# 輸入兩個數字, 轉int
a, b = map(int, input().split())

# 輸入兩字串
grade, closeness = input().split()

# 輸入字串 轉字元, 固定用list轉
input_str = list(input())

# ====================== print ======================
# 格式化輸出
for key, value in op_dict.items():
    print(f"{key}{value}", end=" ")

print(coupon, remain, sep = ',') # sep 輸出分割符號

print(f"{year:04}/{month:02}/{next_day:02}")

print(f"{year:.1f}")

split() # **會自動忽略** 多個空格，只保留有效的元素。
split(" ") # **不會忽略** 多個空格，會將額外的空格視為分隔符，產生空字串。
# 如果你的輸入有不規則的空格，通常 **使用 `split()`（不帶參數）更好！** 😊

# ====================== 數學計算 ======================
# 取公因數
def gcd(a, b):
    while b != 0:
        a, b = b, a % b  # 使用歐幾里得算法
        # print(a, b)
    return a

# 整除
coupon = points // 10 * 100
# 取餘數
remain = points % 10
# ====================== random ==========================
# 在 Python 中，你可以使用 `random` 模組來生成隨機數、隨機選擇元素等。以下是幾種常見的 `random` 使用方法：

### 1. **生成隨機整數 (`randint`)**
import random
   print(random.randint(1, 10))  # 產生 1 到 10 之間的隨機整數

### 2. **生成隨機浮點數 (`uniform`)**
   print(random.uniform(1.0, 5.0))  # 產生 1.0 到 5.0 之間的隨機浮點數

### 3. **生成隨機數 (`random()`)**
   print(random.random())  # 產生 0.0 到 1.0 之間的隨機浮點數

### 4. **隨機選擇 (`choice`)**
   fruits = ["蘋果", "香蕉", "橘子", "葡萄"]
   print(random.choice(fruits))  # 從列表中隨機選擇一個元素

### 5. **隨機排列 (`shuffle`)**
   numbers = [1, 2, 3, 4, 5]
   random.shuffle(numbers)  # 隨機打亂列表順序
   print(numbers)

### 6. **隨機取樣 (`sample`)**
   numbers = [1, 2, 3, 4, 5]
   print(random.sample(numbers, 3))  # 從列表中隨機選取 3 個不重複元素

# 如果你想要固定隨機數的結果（例如進行測試），可以使用 `random.seed()`：
random.seed(42)  # 設定固定的隨機種子
print(random.randint(1, 10))  # 這樣每次執行都會產生相同的隨機數

# ====================== LIST 處理 ======================
# 使用列表推導式提取每個元素的長度
lengths = [len(item) for item in my_list]

# 增加 list 裡面的元素
# append method: 加入單一元素
my_list.append(object)
# insert method: my_list.insert(位置, 物件)
my_list.insert(position, object)
# extend method: 一次加入多個值、或是想將某個 list 中的元素加到另一個 list 的時候
list_1 = [object1, object2, object3]
list_2 = [object4, object5]
list_1.extend(list_2)

# 移除 list 中的元素
#  remove method: 移除一個 list 中的元素
bad = ['Bad','Smooth Criminal','Speed Demon','Man in the Mirror','Dirty Diana']
bad.remove('Smooth Criminal')
#  pop method: 想要移除這個 list 的最後一個元素的話
list.pop()

# copy list
lst = ['a', 'b', 'c', 'd']
lst_copy = lst[:] #沒有[:]會變成是同一個物件

# 範圍取值方式為：串列[起始值:結束值:間隔值]。
# 取奇數位置的物件，亦即由第一個物件開始取，取值的間隔為 2。
lst = ['p', 'y', 't', 'h', 'o', 'n']
print(lst[::2])

# enumerate function
# 我們也可以使用 Python 中的一個函數來同時取得一個元素在一個 list 中的 index 與他的值。
for index, item in enumerate(list_name):
    print(index, item)

#  List Comprehension: 想要把 list 中的數字都存成整數的形態
lst = [int(num) for num in input().split()]
print(lst)

# cclub教材
https://medium.com/ccclub/ccclub-python-for-beginners-tutorial-f1b4e7d2e5ac

# ===================== 資料型態 =====================
# Python 的內建型態主要分為以下三種：
# 數值型態：int, float, bool
# 字串型態：str, chr
# 容器型態：list, dict, tuple

# 字串相加
str1 = "Lucy in the sky"
str2 = " with diamonds"
print(str1 + str2)
# 重複印出字串
str = "ccClub"
print(str*3)

# swapcase() 方法來進行大小寫置換
# upper(): 將字串中的所有字母轉換為大寫 
# lower(): 將字串中的所有字母轉換為小寫
# capitalize(): 將字串的第一個字母轉換為大寫，其餘字母轉換為小寫 
# title(): 將每個單詞的首字母轉換為大寫，其餘字母轉換為小寫

# ====================== 例外處理 try-except =====================
Value Error: 
# 如果本來的值就無法這樣轉換 (例如想要把字串轉換成整數)，就會出現 

    try:
        print(int(num[-1]) + int(num[-2]) + int(num[-3]))
    except(IndexError):
        pass
# ====================== 誤區 ======================
# 字串用 find 找到第一個符合特定值的index
str.find(value)
# 字串用 rfind 找到最後一個符合特定值的index
str.rfind(value)
# list 用 remove 移除特定值
list.remove(value)
# ======================= 字串處理 ====================
text = "hello"
reversed_text = text[::-1]  # 反轉字串
print(reversed_text)  # 輸出：'olleh'

str.isupper() #判斷是否為大寫
# 字串是否為字母
str.isalpha()
# 排除非字母的字符，例如空格
unique_letters = {char for char in unique_letters if char.isalpha()}

# 字首轉大寫
word.capitalize()
# ======================= 型別轉換 ==========================
# list to string
my_list = ['apple', 'banana', 'cherry']
my_string = ', '.join(my_list) 

# ======================= SORT =========================
# 排序 sort(only for list), other type use sorted
# 1
str_xamp = ["sss"]
str_xamp.sort(reverse=True) # 大到小要寫 reverse=True, 不用重新指定變數, 會改變原先list
# 2
a = sorted(iterable_sequence, reverse=True)
# example

# 字串反轉
def sort_by_reversed_strings(string_list):
    # 按照反轉字符串的結果進行排序
    return sorted(string_list, key=lambda x: x[::-1])
input_list = input()
input_list = input_list.split()
sorted_list = sort_by_reversed_strings(input_list)
print(sorted_list)

# 給定一個 list ，排序規則：依照數字的每個位數總和（ex：123 的各個位數總和為 6 ），由小到大排，並且輸出。
def sort_by_digit_sum(number_list):
    # 按數字各位數字之和排序
    return sorted(number_list, key=lambda x: sum(int(digit) for digit in str(x)))

# 示例列表
input_list = [123, 456, 789, 234, 12]
sorted_list = sort_by_digit_sum(input_list)
print("根據位數總和排序後的列表:", sorted_list)
;

s = input()
op = s.split()
op_dict = {int(op_str): xfer(op_str) for op_str in op}
# sorted(op_dict.items()) # 按照key排序

# 按照value小到大排序, 務必要將tuple轉回list 
# item[1] 對value做排序 # item[0] 對key做排序
# lambda x:x[i] x代表tuple第i個元素 做排序
a = dict(sorted(op_dict.items(), key=lambda item:item[1])) 

# b = sorted(op_dict.items(), key=lambda item:item[1], reverse=True) # 大到小
print(list(a.keys())) #要再轉回list輸出

# sort說明
https://blog.csdn.net/a857553315/article/details/79575623
https://www.cnblogs.com/xyao1/p/11022127.html#:~:text=%E7%9B%B4%E6%8E%A5%E4%BD%BF%E7%94%A8sorted%20%28my_dict.keys%20%28%29%29%E5%B0%B1%E8%83%BD%E6%8C%89key%E5%80%BC%E5%AF%B9%E5%AD%97%E5%85%B8%E6%8E%92%E5%BA%8F%EF%BC%8C%E8%BF%99%E9%87%8C%E6%98%AF%E6%8C%89%E7%85%A7%E9%A1%BA%E5%BA%8F%E5%AF%B9key%E5%80%BC%E8%BF%9B%E8%A1%8C%E6%8E%92%E5%BA%8F%E7%9A%84%EF%BC%8C%E5%A6%82%E6%9E%9C%E6%83%B3%E6%8C%89%E7%85%A7%E5%80%92%E5%BA%8F%E6%8E%92%E5%BA%8F%E7%9A%84%E8%AF%9D%EF%BC%8C%E5%8F%AA%E9%9C%80%E8%A6%81%E5%B0%86reverse%E7%BD%AE%E4%B8%BAtrue%E5%8D%B3%E5%8F%AF%E3%80%82,%EF%BC%881%EF%BC%89key%E4%BD%BF%E7%94%A8lambda%E5%8C%BF%E5%90%8D%E5%87%BD%E6%95%B0%E5%8F%96value%E8%BF%9B%E8%A1%8C%E6%8E%92%E5%BA%8F%20%EF%BC%882%EF%BC%89%E5%B0%86key%E5%92%8Cvalue%E5%88%86%E8%A3%85%E6%88%90%E5%85%83%E7%BB%84%EF%BC%8C%E5%86%8D%E8%BF%9B%E8%A1%8C%E6%8E%92%E5%BA%8F%20%E6%88%91%E4%BB%AC%E9%80%9A%E8%BF%87%E4%BE%8B%E5%AD%90%E6%9D%A5%E8%AF%A6%E7%BB%86%E8%A7%A3%E9%87%8A%E4%B8%80%E4%B8%8B%E5%87%BD%E6%95%B0sorted%E7%9A%84%E5%85%B7%E4%BD%93%E7%94%A8%E6%B3%95%EF%BC%9A

# list to dict
https://geek-docs.com/python/python-ask-answer/16_python_convert_list_into_a_dictionary.html

# ======================== 字典 ============================
# init dicts
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = dict(zip(keys, values))

# 濾除 dict
filtered_dict = {key: value for key, value in area_dict.items() if key in wish_lst}
print(filtered_dict)  # {'name': 'Alice', 'country': 'Taiwan'}

# sorted dict
sorted_dict = {key: value for key, value in sorted(area_dict.items(), key=lambda item: item[1])}
print(sorted_dict)  # {'banana': 1, 'cherry': 2, 'apple': 3}
# ======================== 練習題 ======================
# 輸入母音數量
a = str(input())
b = "AEIOUaeiou"
d = []
for i in range(0, len(a)):
    if(a[i] in b):
        d.append(a[i])
print(len(list(set(d))))

# 輸出最小字串
def longest_str(l):
    lis = l.split()
    a=-1
    b=""
    for i in lis:
        if len(i)>a:
            b = i
            a = len(i)
    print(b)    
