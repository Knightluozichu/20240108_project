# 请用户输入三个不同的整数, 输入时用逗号(,)隔开, 利用条件语句判断出这三个整数中的最大值
def maxInputThreeNumber():
    sipt = input("请输入三个不同的整数, 输入时用逗号(,)隔开: ")
    sipt = sipt.split(",")
    a = int(sipt[0])
    b = int(sipt[1])
    c = int(sipt[2])
    # max = max(a, b, c)
    # if max == a:
    #     print(f"最大值是第一个数为: {a}")
    # elif max == b:
    #     print(f"最大值是第二个数为: {b}")
    # else:
    #     print(f"最大值是第三个数为: {c}")

    if a > b and a > c:
        print(f"最大值为: {a}")
    elif b > a and b > c:
        print(f"最大值为: {b}")
    else:
        print(f"最大值为: {c}")


maxInputThreeNumber()

"""
给你一个整数数组 arr, 实现程序： 判断数组中是否存在连续三个元素都是奇数的情况: 如果存在，请输出 True; 否则输出 False
示例 1:
输入: arr = [2, 6, 4, 1]
输出: False
解释: 不存在连续三个元素都是奇数的情况

示例 2:
输入: arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]
输出: True
解释: 存在连续三个元素都是奇数的情况，即 [5, 7, 23]
"""


def isAnOddNumber(x):
    return x % 2 == 1


# def f(i, arr):
#     if i >= len(arr) - 2:
#         return False
#     else:
#         if isAnOddNumber(arr[i]):
#             if isAnOddNumber(arr[i + 1]):
#                 if isAnOddNumber(arr[i + 2]):
#                     return True
#                 else:
#                     return f(i + 3, arr)
#             else:
#                 return f(i + 2, arr)
#         else:
#             return f(i + 1, arr)


def f2(arr):
    i = 0
    while i < len(arr) - 2:
        if isAnOddNumber(arr[i]):
            if isAnOddNumber(arr[i + 1]):
                if isAnOddNumber(arr[i + 2]):
                    return True
                else:
                    i += 3
            else:
                i += 2
        else:
            i += 1
    return False


def verificationFunction():
    arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]
    print(f2(arr))
    arr = [2, 6, 4, 1]
    print(f2(arr))


verificationFunction()
