def insert_sot(nums):
    # 第两个位置 即：序列1   到最后一个位置 即：序列：len(列表)-1
    for i in range(1, len(nums)):       # 遍历出来的是哪个位置上的数据需要插入到已经排好序的列表中
        for j in range(i,0,-1):
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]




if __name__ == '__main__':
    nums = [10, 1, 35, 61, 89, 36, 55]
    insert_sot(nums)
    print(nums)