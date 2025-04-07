def bubble_sort(array):

    count = len(array) - 1

    for i in range(count):       # 循环的总轮数
        # 设置一个标志，如果在某一轮循环的比较中没有发生交换，则说明该序列已经变成有序的了，
        #     如果发生了交换则可以把该标志位改为False，在下一轮比较开始，标志位也会被更新
        temp_c = True
        for j in range(count - i):      # 每轮比较的总次数,每轮比较出的最后一个都不需要再比较了
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
                temp_c = False
        if temp_c:
            # print(f"总共循环了{i}轮")
            break


if __name__ == '__main__':
    num = [10, 1, 35, 61, 89, 36, 55]
    bubble_sort(num)
    print(num)