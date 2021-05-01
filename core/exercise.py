import math


# python 命名规则
# 模块、类、函数、变量、常量的命名需要见名知意，命名的规则如下

# 1. 模块命名
#   模块推荐使用小写命名，
#   除非有很多字母，尽量不要用下划线

# 2. 类命名
#   类名使用驼峰(CamelCase)命名风格，首字母大写
#   私有类可用一个下划线开头

# 3. 函数命名
#   函数名一律小写，如有多个单词，用下划线隔开
#   类内部函数命名，用单下划线(_)开头（该函数可被继承访问）
#   类内私有函数命名，用双下划线(__)开头（该函数不可被继承访问）

# 4. 变量命令
#   变量名推荐小写，如有多个单词，用下划线隔开
#   类内部变量命名，用单下划线(_)开头（该变量可被继承访问）
#   类内私有变量命名，用双下划线(__)开头（该变量不可被继承访问）

# 5. 常量命令
#   使用下划线分割大些字母命名

# date: 20210428
# 1. 请设计一个函数，函数的输入是数字，打印这个数是奇数还是偶数


def judge(num: int):
    print(str(num) + "是奇数") if num % 2 == 0 else print(str(num) + "是偶数")


# 2. 请设计一个函数，输入是半径，返回值是对应圆的面积


def circle_area(radius: int):
    return radius * radius * math.pi


# 3. 给到一个列表，请计算列表中所有元素之和

def list_sum(source):
    result = 0
    for num in source:
        result += num
    return result


# 4. 给到一个列表，请计算出列表中所有偶数之和

def list_even_sum(source):
    result = 0
    for num in source:
        if num % 2 == 0:
            result += num
    return result


# 5. 给到一个列表，请计算出列表中所有素数之和

# 判断数字是否为素数,设计为一个函数是因为下面还要使用
def judge_prime(num):
    if num <= 1:
        return False
    half_num = num // 2
    for i in range(2, half_num + 1):
        if num % i == 0:
            return False
    return True


def list_prime_sum(source):
    result = 0
    for num in source:
        if judge_prime(num):
            result += num
    return result


# 6. 将 3，4，5 封装成函数，函数的输入是列表，函数的返回值为对应的和
# 7. 请打印出 1-100 之间所有的素数


# 8. 请设计一个函数，打印指定范围的素数
def print_prime(start, end):
    for i in range(start, end):
        if judge_prime(i):
            print(i)


# 9. 请设计一个函数，输入是一个范围，返回时这个范围内的所有素数
def get_prime(start, end):
    result = []
    for i in range(start, end):
        if judge_prime(i):
            result.append(i)
    return result


# 202010429
# 10. 冒泡排序 核心:两两交换，娜位置，到最后的就是最大的数
def sort_bubble(arr):
    for i in range(len(arr)):
        for k in range(len(arr) - i - 1):
            if arr[k] > arr[k + 1]:
                arr[k], arr[k + 1] = arr[k + 1], arr[k]


# 11. 选择排序 核心: 每次循环找到最小的，找到就和当前循环对于的索引位置交换
# 方法1 找到就交换
def sort_select1(arr):
    for i in range(len(arr)):
        for k in range(i + 1, len(arr)):
            if arr[k] < arr[i]:
                arr[i], arr[k] = arr[k], arr[i]


# 方法2 记录每次循环最小值的索引，最后交换
def sort_select2(arr):
    for i in range(len(arr)):
        min_index = i
        for k in range(i + 1, len(arr)):
            if arr[k] < arr[min_index]:
                min_index = k
        arr[i], arr[min_index] = arr[min_index], arr[i]


# 方法1 和 方法2 的区别:
#   方法1 要多交换几次
#   方法2 要多存一个变量 min_index
# 推荐使用 2

# 20210501
# 1.请设计一个函数，查找列表中的最小的元素
def find_min(arr):
    result = arr[0]
    for ele in arr:
        if ele < result:
            result = ele
    return result


# 2.现在有一个字典，key的类型为字符串，value类型为int，请设计一个函数，求所有的value之和
# 方法1 拿到所有的 key，通过 key 找到 value，求和
def dict_values_sum1(dictionary):
    result = 0
    for key in dictionary:
        result += dictionary[key]
    return result


# 方法2 拿到所有的 key,value,对 value 求和
def dict_values_sum2(dictionary):
    result = 0
    for key, value in dictionary.items():
        result += value
    return result


# 方法3 拿到所有的 value，求和
def dict_values_sum3(dictionary):
    result = 0
    for value in dictionary.values():
        result += value
    return result


# 补充内容:
#   列表遍历的两种方式
# 方法1 通过索引遍历
def list_traverse1(arr):
    for index in range(len(arr)):
        print(arr[index])


# 方法2 直接遍历
def list_traverse2(arr):
    for ele in arr:
        print(ele)


# 3.现在有一个排好序的列表，请设计一个函数:
#   函数的输入是一个元素
#   函数内部使用二分查找查找该元素
#   如果查找成功，则返回该元素对应的索引
#   如果列表中不存在该元素，则返回None
def binary_search(arr, target):
    pass


# 4.现在给到一个列表，请统计列表中各元素的个数
# 方法1 和 方法2 思路
#   遍历列表，将结果放入到字典中，其中 key 为对应的元素，value 为次数，
#   如果字典中不存在该元素，则对应的 value 设置为1
#   如果字典中存在该元素，则对应的 value +1
# 方法1
def list_element_count1(arr):
    result = {}
    for ele in arr:
        if ele in result.keys():
            result[ele] += 1
        else:
            result[ele] = 1
    return result


# 方法2
def list_element_count2(arr):
    result = {}
    for ele in arr:
        if result.get(ele):
            result[ele] += 1
        else:
            result[ele] = 1
    return result


# 方法3 使用 list 中 count() 方法求每个元素的数量
def list_element_count3(arr):
    result = {}
    for ele in arr:
        result[ele] = arr.count(ele)
    return result

# 推荐使用方法2，时间复杂度最小
