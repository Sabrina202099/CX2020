"""
flags扩展功能演示
"""
s="""Hello
北京
"""
import re
regex=re.compile(r'\w+',flags=re.A)
l=regex.findall(s)
print(l)

regex=re.compile(r'[a-z]+',flags=re.I)
l=regex.findall(s)
print(l)

regex=re.compile(r'.+',flags=re.S)
l=regex.findall(s)
print(l)