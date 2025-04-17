'''
    Tim排序：


'''


# TimSort 依赖于插入排序和归并排序，首先实现这 2 种排序。
# insertionSort函数用插入排序从left到right排序数组arr
def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


# merge函数合并排序好的run块
def merge(arr, l, m, r):
    # 原数组一分为二：左数组和右数组
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])

    i, j, k = 0, 0, l

    # 比较后将两个数组合并成一个更大的数组
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k] = right[j]
            j += 1

        k += 1

    # 复制左数组遗留元素
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1

    # 复制右数组遗留元素
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1

# 计算 run 块的最小值，确保归并可以高效运行
MIN_MERGE = 32

# 计算run块的最小长度
def calcMinRun(n):
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r

# TimSort过程
# TimSort排序
def timSort(arr):
    n = len(arr)
    minRun = calcMinRun(n)

    # 对大小为 RUN 的单个子数组进行排序
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(arr, start, end)

    # 从大小 RUN（或 32）开始合并。最终合并形成大小为2^n
    size = minRun
    while size < n:
        # 选择左子数组的起点。
        # 合并 arr[left..left+size-1] 和 arr[left+size, left+2*size-1]
        # 每次合并后，left 增加 2*size
        for left in range(0, n, 2 * size):
            # 查找左子数组的终点
            # mid+1 为右子数组的起点
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            # 合并子数组 arr[left.....mid] & arr[mid+1....right]
            if mid < right:
                merge(arr, left, mid, right)

        size = 2 * size


if __name__ == "__main__":
    arr = [-2, 7, 15, -14, 0, 15, 0, 7, -7, -4, -13, 5, 8, -14, 12]

    print("排序前")
    print(arr)

    timSort(arr)

    print("排序后")
    print(arr)

