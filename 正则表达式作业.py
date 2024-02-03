"""
匹配string中所有单词的开头字母

string = 'Then your voice calls me back like a wake up call'
"""

# import re
# p = re.compile(r"\b[a-zA-Z]")
# m = p.findall("Then your voice calls me back like a wake up call")
# print(m)


"""
匹配string中除了数字以外的单词

string = 'This dog has been with me for 5 years and 11 months'
"""

# import re
# p = re.compile(r"\b[a-zA-Z]+\b")
# m = p.findall("This dog has been with me for 5 years and 11 months")
# print(m)


"""
提取出string中的所有域名(比如: http://www.iteoem.com/ 就是域名)

string = '''
http://www.iteoem.com/messageinfo.asp?id=35
http://3995503.com/class/class09/news_show.asp?id=14
http://lib.wzmc.edu.cn/news/onews.asp?id=769
http://www.zy-ls.com/alfx.asp?newsid=377&id=6
http://www.fincm.com/newslist.asp?id=415
'''
"""

import re

# p = re.compile(r"http://.+?/", flags=re.MULTILINE)
# m = p.findall(
#     """
# http://www.iteoem.com/messageinfo.asp?id=35
# http://3995503.com/class/class09/news_show.asp?id=14
# http://lib.wzmc.edu.cn/news/onews.asp?id=769
# http://www.zy-ls.com/alfx.asp?newsid=377&id=6
# http://www.fincm.com/newslist.asp?id=415
# """
# )
# print(m)


"""
提取string中连续5个以上的数字

string = '小明202208月见义勇为, 替小红当了3456789点暴击伤害, 快打110报警, 抓住那个劫匪'
"""

# import re
# p = re.compile(r"\d{5,}")
# m = p.findall("小明202208月见义勇为, 替小红当了3456789点暴击伤害, 快打110报警, 抓住那个劫匪")
# print(m)

"""
判断一个字符串是否是ip地址
规则: 一个ip地址由4个数字组成, 每个数字之间用.连接, 每个数字的大小是0-255

比如:
255.189.10.37 正确
256.189.89.9 错误
"""

# 0-99 [0-9]{1,2}
# 100-199 1[0-9]{2}
# 200-249 2[0-4][0-9]
# 250-255 25[0-5]


# import re

# p = re.compile(r"""
#                                         (?:(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})[.]){3}
#                                         (?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})
#                                         """, re.VERBOSE)
# m = p.match("255.189.10.37")
# print(m)
# m1 = p.match("256.189.89.9")
# print(m1)
# m2 = p.match("8.9.9.0")
# print(m2)


"""
计算一个字符串中所有的数字的和

比如:  string = 'hello90abc 78sjh12.5'
结果:  180.5 (90 + 78 + 12.5)
"""
import re

# p = re.compile(r"\d+\.?\d*")
# m = p.findall("hello90abc 78sjh12.5")
# # print("+".join(m) + "=" + str(sum(map(float, m))))
# print(eval("+".join(m)))

"""
用*号隐藏电话号码的中间四位数

比如:  phone = '13841789213'
结果:  '138****9213'
"""
# import re
# p = re.compile(r"(\d{3})\d{4}(\d{4})")
# m = p.sub(r"\1****\2", "13841789213")
# print(m)


"""
提取string中以m或t开头的单词, 忽略大小写

string = 'This module provides regular expression matching operations similar to those found in Perl'
"""
# import re

# p = re.compile(r"\b[mt][a-z]*", re.I)
# m = p.findall(
#     "This module provides regular expression matching operations similar to those found in Perl"
# )
# print(m)
