# 归并  分治法
def merge_sort(nums):

    # 拆分
    if len(nums) <= 1:      # 如果只有一个元素，则直接返回
        return nums

    count = len(nums) // 2       # 获取中间索引的值
    left = merge_sort(nums[:count])
    right = merge_sort(nums[count:])

    # 合并
    return merge(left, right)


def merge(left, right):
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += list(left[l:])
    result += list(right[r:])

    return result

if __name__ == '__main__':


    nums = [10, 1, 35, 61, 89, 36, 55]
    print(merge_sort(nums))