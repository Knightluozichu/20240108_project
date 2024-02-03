import re


# p = re.compile(r'.ab') #任意字符
p = re.compile(r".")

m = p.findall(" ")

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
'''
1.是字符串匹配正则表达式，而不是正则表达式匹配字符串
2.正则表达式要匹配完全才算匹配成功
3.贪婪模式或非贪婪模式，前提是要匹配成功
4.正则表达式是字符串，所以不要随意加空格
'''
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