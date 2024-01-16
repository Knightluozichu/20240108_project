def python_01():
    print("执行第1行啦")
    print(2 / 1)
    print("执行第3行啦")
    a = 123
    print(a)

    def add(left, right):
        print("执行第9行啦")
        print("执行第10行啦", left + right)

    print("执行第13行啦")
    add(3, 4)
    a = 124
    print(a)
    print("执行第17行啦")


def python_03():
    """
    1. 缩进,是语法是格式,不一定是4个空格,但是要保持一致,[条件语句-循环语句-函数定义],用来表示代码的层次结构
    2. 注释：#  单行注释, """ """  多行注释
    3. 拼接: 显示的-反斜杠, 或者隐式的-用括号括起来
        a = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
        a = 1 + 2 + 3 + 4 + 5 + \
            6 + 7 + 8 + 9 + 10
        a = (1 + 2 + 3 + 4 + 5 +
             6 + 7 + 8 + 9 + 10)
    4. 变量: 用来存储数据的容器,先定义再使用,变量名=值,
        a.标识符的命名规则: 1. 由数字,字母,下划线组成 2. 不能以数字开头 3. 不能是关键字
        b.变量名是标识符,用于变量-函数-类-模块-包等的名称
        c.关键字查询
    5. 內置函數: 
        a.python解釋器内置了很多函数和类型,可以直接使用
        b.查看内置函数: dir(__builtins__)以及    import builtins    print(dir(builtins))
    6. 常量: 用来存储不变的数据,一般用大写字母表示,但是python没有常量的概念,只是约定俗成
    7. 输出: print(*values, sep='', end='\n', file=sys.stdout, flush=False)
    8. 输入: input([prompt]) 接受一个标准输入数据,返回为字符串类型
    """

    # import keyword

    # print(keyword.kwlist)
    # print(dir(__builtins__))

    # import builtins

    # print(dir(builtins))

    # PI = 3.1415926

    # print(1, 2, 3, sep="-", end="-456")

    # with open("./01_write.txt", "w") as f:
    #     print("123", file=f)

    # import time

    # # 不使用flush，输出会在循环结束后一次性显示
    # for i in range(5):
    #     print(".", end="", flush=False)
    #     time.sleep(0.5)
    # print()

    # # 使用flush，输出会在每次循环时立即显示
    # for i in range(5):
    #     print(".", end="", flush=True)
    #     time.sleep(0.5)

    ipt = input("请输入:")
    print("输入[" + ipt + "]结束")
    abs(-1)


# python_03()
