import re

userinput='asd'
pattern ='^[0-9][A-Z].*o$'
a=re.match(pattern,userinput)
if a:
    print("match")
else:
    print("unmatch")
re.findall
re.search