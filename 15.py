# import re


# p = re.compile(r'.ab') #任意字符
# p = re.compile(r".")

# m = p.findall(" ")

# p = re.compile(r'.ab', re.DOTALL) #忽略换行符
# p = re.compile(r'^ab') # 匹配字符串开头
# p = re.compile(r"^ab", re.MULTILINE) # 匹配每行开头
# p = re.compile(r"ab$", re.MULTILINE) # 匹配每行结尾
# 对前一个字符做赋能，* 匹配0次或多次, + 匹配1次或多次, ? 匹配0次或1次,{m,n} 匹配m到n次
# 以上三种特殊符号，默认都是贪婪模式,在上面特殊符号后面加?,非贪婪模式
# | 匹配左右任意一个表达式, 匹配到一个就不再匹配
# \ 转义字符 或者 表示特殊序列
# 反斜杠问题，如果不是特殊序列，就是反斜杠本身
# 规则
"""
1.是字符串匹配正则表达式，而不是正则表达式匹配字符串
2.正则表达式要匹配完全才算匹配成功
3.贪婪模式或非贪婪模式，前提是要匹配成功
4.正则表达式是字符串，所以不要随意加空格
"""
# muxTex = "ab..ab.abpoo\nabcab"

# m = p.findall(muxTex)

# print(m)

# p = re.compile(r"ab?")
# m = p.search("abbbbccd")
# print(m)

# 题目请写一个正则表达式去匹配字符串中的单词'cat'
# p = re.compile(r"cat")
# word = "**cat c"
# m = p.search(word)
# print(m)

# 题目请写一个正则表达式去匹配字符串中的单词'cat' 和 'hat'
# 字符串是"**cat c hat h"
# p = re.compile(r"[ch]at")
# word = "**cat c hat h"
# m = p.findall(word)
# print(m)

# Sure! Here are three regex-related questions for you:

# 1. Write a regular expression pattern that matches any string containing the word "cat".
# 2. Write a regular expression pattern that matches a valid email address.

# p = re.compile(r"^[0-9]{5,11}@qq\.com$")
# p = re.compile(r"^[a-zA-Z0-9_-]+@163\.com$")
# m = p.match("luozichu@bilibili.com")
# m1 = p.match("rainknightpox@gmail.com")
# m2 = p.search("qwep13928245451@163.com")
# m3 = p.search("qwep13928245451@1asd63.com123")
# m4 = p.search("931686160@qq.com")
# print(m,m1)

# 3. Write a regular expression pattern that matches a phone number in the format XXX-XXX-XXXX.

# p = re.compile(r"^[0-9]{3}-[0-9]{3}-[0-9]{4}$")

# Give them a try and let me know if you need any help!

# 特殊序列 由\和一个字符组成的特殊序列
"""
\number 匹配数字代表的分组里面的内容，每个括号代表一个子组，从1开始。
在[和]字符集内，任何数字转义都被看作是字符
"""

# p = re.compile(r"(.+) \1")
# print(p.search("ab abc"))


"""
\A 匹配字符串的开头，类似于 ^ ，区别在于：MULTILINE模式下， \A 不识别换行
\Z 匹配字符串的末尾，且 MULTILINE 模式下， \Z 不识别换行
"""

# import re

# p = re.compile(r"^ab")
# print(p.findall("abcd\nabfg"))
# p = re.compile(r"^ab", flags=re.MULTILINE)
# print(p.findall("abcd\nabfg"))

# p = re.compile(r"\Aab")
# print(p.findall("abcd\nabfg"))
# p = re.compile(r"\Aab", flags=re.MULTILINE)
# print(p.findall("abcd\nabfg"))

"""
\b 匹配空字符串，但是只在单词的开头或结尾，即匹配一个单词边界 不分中英文，但特殊字符不行
\B 匹配空字符串，但不能在单词开始或结尾的位置，即匹配非单词边界
"""

# import re
# p = re.compile(r"er\b")
# print(p.search("never"))
# print(p.search("verb"))
# p = re.compile(r"\ba\b")
# print(p.search("I have a dog"))

# import re
# p = re.compile(r"er\B")
# print(p.search("never"))
# print(p.search("verb"))

"""
\d 匹配任何一个十进制个位数数字，等价于 [0-9]
\D 匹配任何一个非数字字符，等价于 [^0-9]
"""

# import re

# p = re.compile(r"\d")
# print(p.findall("125634"))
# p = re.compile(r"\D{1,}")
# print(p.findall("12qw5q634"))

"""
\s 匹配任何一个空白字符，等价于 [\t\n\r\f\v]
\S 匹配任何一个非空白字符，等价于 [^\t\n\r\f\v]
"""

# import re
# p = re.compile(r"\S{1,}")
# print(p.findall("a b c"))
# print(p.findall("abc"))
# print(p.findall("a b c\n\t\vpo 0\n"))


"""
\w 匹配一个字母或数字或下划线，等价于 [a-zA-Z0-9_]
\W 匹配一个非字母或数字或下划线，等价于 [^a-zA-Z0-9_]
"""

# import re
# p = re.compile(r"\W")
# print(p.findall("a 90_b c"))
# print(p.findall("a-b+c?"))

"""
\n \t \\ \' \"
绝大部分Python的标准转义字符也被正则表达式分析器识别
"""

# import re
# p = re.compile(r"\\|b")
# print(p.findall(r"a\\b c"))


"""
[] 用于表示一个字符集：
字符可以单独列出，比如 [amk] 匹配 'a' ， 'm' ， 或者 'k'
- 用于表示字符范围，通过-将两个字符连接起来，比如 [a-z] 匹配任何小写字母
特殊字符在字符集内，不再有特殊含义，比如 [akm$] 匹配 'a' ， 'k' ， 'm' 或者 '$'
特殊序列在字符集内，有特殊含义，比如 [a-d\w] 匹配 'a' ， 'b' ， 'c' ， 'd' 或者 字母或数字或下划线
^ 表示字符集的补集，即匹配不在字符集内的字符,但是需要^在字符集内首位，否则^在字符集内，就是普通字符，不是补集
如果要匹配[],需要转义
"""

# import re

# p = re.compile(r"[amk]")
# print(p.findall("a pop 12nm2 kkk"))
# p = re.compile("[a-z]")
# print(p.findall('io P91+12/n\n'))
# p = re.compile(r"[o$]")
# print(p.findall("o oad $so"))
# p = re.compile(r"[a-d\w]")
# print(p.findall(r"d012——_p"))
# p = re.compile(r"[^amk]|[\[\]]")
# print(p.findall("mk_2+?e[wr\\a"))

"""
(...)
捕获分组 匹配括号内的任意正则表达式，并表示出该分组的开始和结尾
组从0开始编号，组0始终存在，它表示整个正则，所以Match的对象方法都将组0作为默认参数，子组从左到右编号，从1向上编号
分组匹配的内容可以在之后其他分组用\number进行再次引用
要匹配字符(和),需要使用转义字符，或者包含在字符集里面

(?:...)
非捕获分组，并不创建新的组合，所匹配的子字符串不能在执行匹配后被获取或是
之后在模式中被引用

(?=...) 前向肯定界定符，并不创建新的组合，且括号内的正则表达式匹配成功时才能继续匹配，否则整个匹配失败
(?!...) 前向否定界定符，并不创建新的组合，且括号内的正则表达式匹配失败才能继续匹配，否则整个匹配失败
"""

# import re
# p = re.compile(r"b(.+)a(.+)e")
# m = p.match("babacdefg")
# print(m)
# print(m.group(1), m.group(2))
# print(m.groups())
# print(m.span(1), m.span(2))
# print(m.start(1), m.end(1))
# print(m.start(2), m.end(2))
# # 多个分组，返回元组列表
# print(p.findall("babacdefg"))
# # 引用第1组匹配的内容
# p = re.compile(r"b(.+)a(\1)e") #⚠️注意："b(.+)a(\1)e" !== "b(.+)a(.+)e"
# m = p.match("babaabefg")
# print(p.match("babaabefg"))
# print(m.group(1))
# print(m.group(2))

# import re

# p = re.compile(r"b(?:.+)a(.+)e")
# m = p.match("babacdefg")
# print(m)
# print(m.groups())

# import re

"""
第一步： .+[.] 匹配成功
第二步： 前向肯定界定符匹配成功才继续第三步，否则匹配失败
第三步： .+ 接着第一步继续匹配
最后结果为第一步和第三步匹配的结果 """
# p = re.compile(r".+[.](?=exe$).+")
# m = p.match("ab.exe")  # 文件名必须以exe为后缀
# print(m)


import re

"""
第一步： .+[.] 匹配成功
第二步： 前向否定界定符匹配失败才继续第三步，否则匹配失败
第三步： .+ 接着第一步继续匹配
最后结果为第一步和第三步匹配的结果 """
# p = re.compile(r".+[.](?!exe$|txt$).+")
# m = p.match("ab.txt") # 文件名不能以exe或txt为后缀
# print(m)


# import re

# p = re.compile(r"""
#                                         \d+ #一个数字字符,至少一位,不限制位数，贪婪模式
#                                         .   #一个任意字符，除了换行符
#                                         \d* #一个数字字符，0个或多个，贪婪模式
#                                         """, re.VERBOSE)
# m = p.findall("1.23456.78")

# print(m)

# import re
# p = re.compile(r"a(bc).(.+)p")
# m = p.findall("abcpabcp")
# print(m) # [('bc', 'abc')]
