# string = 'hello world', string[1 : 8 : 2]的结果是什么?

"el o"

# string = 'hello world', string[-2 : 4 : -2]的结果是什么?
"lo "

# string = 'hello world', string[: 6]的结果是什么?
"hello "

"""
编写一个程序, 帮助水果店实现计价功能:
请用户输入水果品种, 水果单价(元/kg)和重量(kg),
计算出需要花费的金额并输出

例:
用户输入水果品种为: 苹果
输入单价为: 3.98
输入重量为: 2.58
计算出总价为: 10.2684

请用三种格式化方式输出如下结果:
您购买了2.58kg的苹果, 单价为3.98元/kg, 您需要支付10.27元!
"""
# %格式化

sInputfruit = input("请输入水果品种:")
sInputfruitUnit = input("请输入水果单价:")
sInputfruitWeight = input("请输入水果重量:")
# sInputfruit = "苹果"
# sInputfruitUnit = "3.98"
# sInputfruitWeight = "2.58"
fInputfruitUnit = float(sInputfruitUnit)
fInputfruitWeight = float(sInputfruitWeight)
sInputfruitTotal = fInputfruitUnit * fInputfruitWeight
print("\n\n" + "%格式化".center(50, "-"))
print(
    "例:\n"
    "用户输入水果品种为: %s\n输入单价为: %.2f\n输入重量为: %.2f\n计算出总价为: %f\n"
    % (sInputfruit, fInputfruitUnit, fInputfruitWeight, sInputfruitTotal)
)
print(
    "您购买了%.2fkg的苹果, 单价为%.2f元/kg, 您需要支付%.2f元!\n\n"
    % (fInputfruitWeight, fInputfruitUnit, sInputfruitTotal)
)

# format格式化
print("\n\n" + "format格式化".center(50, "-"))
print(
    "例:\n"
    "用户输入水果品种为: {}\n输入单价为: {}\n输入重量为: {:.2f}\n计算出总价为: {}\n".format(
        sInputfruit, fInputfruitUnit, fInputfruitWeight, sInputfruitTotal
    )
)
print(
    "您购买了{:.2f}kg的苹果, 单价为{:.2f}元/kg, 您需要支付{:.2f}元!\n\n".format(
        fInputfruitWeight, fInputfruitUnit, sInputfruitTotal
    )
)
# f-string格式化
print("\n\n" + "f-string格式化".center(50, "-"))
print(
    "例:\n"
    f"用户输入水果品种为: {sInputfruit}\n输入单价为: {fInputfruitUnit}\n输入重量为: {fInputfruitWeight:.2f}\n计算出总价为: {sInputfruitTotal}\n"
)
print(
    f"您购买了{fInputfruitWeight:.2f}kg的苹果, 单价为{fInputfruitUnit:.2f}元/kg, 您需要支付{sInputfruitTotal:.2f}元!\n\n"
)
