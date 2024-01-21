"""
定义函数实现: 对于一个任意的正整数, 判断其是否为阿姆斯特朗数。

如果一个n位正整数等于其各位数字的n次方之和, 则称该数为阿姆斯特朗数。 例如1^3 + 5^3 + 3^3 = 153。

1000以内的阿姆斯特朗数:  1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。
"""


def isItAnArmstrongNumber(x):
    sNum = str(x)
    sLen = len(sNum)
    sum = 0
    for i in range(sLen):
        sum += int(sNum[i]) ** sLen
    return sum == x


def verificationIsItAnArmstrongNumber():
    lst = []
    for i in range(1000):
        if isItAnArmstrongNumber(i):
            lst.append(i)
    print(f"1000以内的阿姆斯特朗数: {lst}\n")


verificationIsItAnArmstrongNumber()

"""
给你一个数组 nums, 数组中有2n个元素, 按 [x1,x2,...,xn,y1,y2,...,yn] 的格式排列。

请你定义函数将数组按 [x1, y1, x2, y2,..., xn, yn] 格式重新排列, 返回重排后的数组。

示例 1: 
输入: nums = [2, 5, 1, 3, 4, 7], n = 3
输出: [2, 3, 5, 4, 1, 7] 
解释: 由于 x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 , 所以答案为 [2, 3, 5, 4, 1, 7]

示例 2: 
输入: nums = [1, 2, 3, 4, 4, 3, 2, 1], n = 4
输出: [1, 4, 2, 3, 3, 2, 4, 1]

示例 3: 
输入: nums = [1, 1, 2, 2], n = 2
输出: [1, 2, 1, 2]
"""


def formatRearrange(nums, n):
    """
    规则nums的长度一定是2n
    从列表中取出xn, yn, 依次插入到新列表中
    """
    lst = []
    for i in range(n):
        lst.append(nums[i])
        lst.append(nums[i + n])
    return lst


# print(formatRearrange([2, 5, 1, 3, 4, 7], 3))
def verificationFormatRearrange(nums, n, vNums):
    print(
        f"""输入: nums = {nums}, n = {n}\n输出:{formatRearrange(nums,n) == vNums}\n"""
    )


def testVerificationFormatRearrange():
    print("测试 formatRearrange 函数:")
    verificationFormatRearrange([2, 5, 1, 3, 4, 7], 3, [2, 3, 5, 4, 1, 7])
    verificationFormatRearrange([1, 2, 3, 4, 4, 3, 2, 1], 4, [1, 4, 2, 3, 3, 2, 4, 1])
    verificationFormatRearrange([1, 1, 2, 2], 2, [1, 2, 1, 2])


testVerificationFormatRearrange()
