"""
Regex 生成match对象函数
"""
import re
s='今年是2020年，建国71周年'
m=re.fullmatch(r'[,\w]+','今年是2020年,建国71周年')
print(m.group())

"""
匹配目标字符串的开始位置
"""
m=re.match(r'\w+',s)
print(m.group())