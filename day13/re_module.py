import re
s="Alex:1998,Sunny:1999"
pattern=r'\w+:\d+'

# l=re.findall(pattern,s)
# print(l)
#
# regex=re.compile(pattern)
# l=regex.findall(s)
# print(l)

l=re.split(r'[:,]',s)
print(l)

l=re.sub(r':','_',s)
print(l)