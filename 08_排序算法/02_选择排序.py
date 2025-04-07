def selector_sort(nums):
    # 从第一个一直比较到最后一个，第一个值索引是0 ，最后一个值的索引是len(nums) - 1
    for j in range(0, len(nums) - 1):
        min_index = j  # 默认将第0位的元素当作最小的
        for i in range(min_index + 1, len(nums)):  # 找到每一轮对应的最小值
            # 将该轮对应的每一个值和每次的最小值进行比较，如果比最小值小，则将该值作为新的最小值
            if nums[i] < nums[min_index]:
                min_index = i
        # print(min_index)
        nums[j], nums[min_index] = nums[min_index], nums[j]


if __name__ == '__main__':
    nums = [10, 1, 35, 61, 89, 36, 55]
    selector_sort(nums)
    print(nums)
