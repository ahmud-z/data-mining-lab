def cal_sum(*nums):
    sum = 0
    for num in nums:
        sum = sum + num
    return sum

sum = cal_sum(1, 2, 3, 4, 5)
print(f"Sum Result: {sum}")