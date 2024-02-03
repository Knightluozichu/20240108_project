# import builtins
# print(dir(builtins))
"""
'ArithmeticError', 'AssertionError', 'AttributeError', 
'BaseException', 'BaseExceptionGroup', 'BlockingIOError', 
'BrokenPipeError', 'BufferError', 'BytesWarning', 
'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 
'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 
'Exception', 'ExceptionGroup', 'False', 'FileExistsError', 'FileNotFoundError', 
'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 
'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError',
'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError',
'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 
'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 
'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 
'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError',
'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning',
'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError'
"""

# try:
#     a = 1 / 1

#     try:
#         a = 1 / 2
#     except ZeroDivisionError:
#         print("try中发生了除数为0的异常")

# except ZeroDivisionError:
#     print("try中发生了除数为0的异常")


# except TypeError:
#     print("try中发生了类型异常")

# else:
#     print("try中没有发生异常")

# finally:
#     print("finally中的代码一定会执行")


# def div(a, b):
#     if b == 0:
#         raise ZeroDivisionError("除数不能为0!!!!!!")
#     else:
#         return a / b


# div(1, 2)


# try:
#     div(1, 0)
# except ZeroDivisionError as e:
#     print(e)


# assert 断言
# assert 用于判断一个表达式，在表达式为 False 的时候触发 AssertionError 异常
# assert expression 等价于
# if not expression: raise AssertionError
# assert expression [, arguments]
# 等价于：if not expression: raise AssertionError(arguments)

try:
    assert 1 != 1, "1不等于1"
except AssertionError as e:
    print(e)


