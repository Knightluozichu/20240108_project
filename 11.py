def outer(a):
    b = 5

    def inner():
        c = 7
        print(a + b + c)

    return inner


inner_O = outer(3)
print(inner_O.__closure__)


'''
这是因为Python的闭包延迟绑定。这意味着内部函数`inner`在每次循环中都被定义，但是它并不立即执行。相反，它在后面被调用时才执行。在那个时候，它引用的`i`已经变成了3，所以`i * i`的结果是9。

如果你想要每个函数返回不同的结果，你需要在创建每个函数时立即绑定`i`的当前值。你可以通过将`i`作为默认参数来实现这一点：

```python
def outer():
    funcs = []
    for i in range(1, 4):
        def inner(i=i):  # 将当前的i作为默认参数
            return i * i
        funcs.append(inner)
    return funcs

f1, f2, f3 = outer()
print(f1(), f2(), f3())  # 输出：1 4 9
```

现在，每个`inner`函数在被创建时都会记住`i`的当前值，所以它们在后面被调用时会返回不同的结果。
'''

def outer():
    funcs = []
    for i in range(1, 4):
        def inner(i=i):
            return i * i

        funcs.append(inner)
    return funcs


f1, f2, f3 = outer()
print(f1(), f2(), f3())
