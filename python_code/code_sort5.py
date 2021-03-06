import numpy as np
import time
from functools import wraps

# 分区，在index左边小于，index右边大于
def partition(a, l, r):
    key = a[l]
    i = l
    for j in range(l+1, r+1):
        if a[j] <= key:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[i] = a[i], a[l]
    return i

# 将index两边排序，终止条件注意
def quickSort_(a, l, r):
    if l < r:
        i = partition(a, l, r)
        quickSort_(a, l, i-1)
        quickSort_(a, i+1, r)

def quickSort(a):
    la = len(a) - 1
    quickSort_(a, 0, la)
    # return a

# 排序两个有序数组
def merge(a, b):
    la = len(a)
    lb = len(b)
    i = j = 0
    result = []
    while i < la and j < lb:
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result += a[i:]
    result += b[j:]
    return result

def mergeSort(a):
    la = len(a)                   # 注意终止条件
    if la <= 1:
        return a
    mid = int(la / 2)
    b = mergeSort(a[:mid])
    c = mergeSort(a[mid:])
    return merge(b, c)

# 进行n-1趟遍历，每趟遍历逐次比较并交换，找到最小或最大的那个。
def mpSort(a):
    la = len(a)
    for i in range(la-1, 0, -1):
        exchange = False
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                exchange = True
        if exchange == False:
            break
    # return a

# 进行n-1趟遍历，每趟遍历逐次与最小（大）值比较，记录index，找到最小或最大的那个。
# 减少交换的次数（但是不稳定）
def xzSort(a):
    la = len(a)
    for i in range(la - 1, 0 , -1):
        max = i
        for j in range(0, i):
            if a[j] > a[max]:
                max = j
        a[max], a[i] = a[i], a[max]
    # return a

# 插入到有序数组里面，每趟从有序数组的后面遍历
def crSort(a):
    la = len(a)
    for i in range(1, la):
        for j in range(i - 1, -1, -1):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
                i -= 1
    
def timeFunc(func):
    # 任意参数的原函数
    @wraps(func)
    def time_testn(*args, **kwargs):
        start = time.clock()
        result = func(*args, **kwargs)
        print(*args, time.clock() - start)
        return result
    return time_testn
    
n = 80
@timeFunc
def testn(a):
    # n = 100
    lista = list(np.random.randint(0, 5000, n))
    lista = a(lista)
    flag = True
    for i in range(n-1):
        if lista[i] > lista[i+1]:
            flag = False
            break
    return flag

# in place
@timeFunc
def testnn(a):
    # n = 100
    lista = list(np.random.randint(0, 5000, n))
    a(lista)
    flag = True
    for i in range(n-1):
        if lista[i] > lista[i+1]:
            flag = False
            break
    return flag
    
print('快排: ', testnn(quickSort))          # 随机更快
print('归并：', testn(mergeSort))           # 不随机更快
print('选择：', testnn(xzSort))             # 较慢，快于插入、冒泡，但不稳定
print('插入：', testnn(crSort))             # 慢，快于冒泡
print('冒泡：', testnn(mpSort))             # 慢
print(testn.__name__)
