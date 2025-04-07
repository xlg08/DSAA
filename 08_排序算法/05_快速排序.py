'''
    @User: LG
    @Auther: http://www.xlonggang.cn
    @Date: 2025/4/5 0005 9:22 
    @Description: 
    @Project ：数据结构 
    @File    ：05_快速排序.py
    @version: 1.0
'''


# 快速排序是冒泡排序的一种改进 ， 具有一些分治法的思想。

def quick_sort(nums):
    if len(nums) >= 2:
        mid = nums[len(nums) // 2]
        left, right = [], []
        nums.remove(mid)
        for d in nums:
            if d < mid:
                left.append(d)
            else:
                right.append(d)
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return nums


if __name__ == '__main__':
    nums = [10, 1, 35, 61, 89, 36, 55]
    nums_new = quick_sort(nums)
    print(nums_new)
