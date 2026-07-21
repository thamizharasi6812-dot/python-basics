# exercise:1
s = "{[(]"

while "()" in s or "[]" in s or "{}" in s:
    s = s.replace("()", "")
    s = s.replace("[]", "")
    s = s.replace("{}", "")

if s == "":
    print(True)
else:
    print(False)

# exercise:2
s= 'pwwkew'
m=''

for i in s:
    if i not in m:
        m=m+i
print(len(m))

# exercise:3
s=['dog','racecar','car']

prefix=s[0]

for word in s:
    while not word.startswith(prefix):
        prefix=prefix[:-1]
print(prefix)