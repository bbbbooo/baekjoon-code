a = input()
b = a.upper()

list = []
abc = 'ABC'
deF = 'DEF'
ghi = 'GHI'
jkl = 'JKL'
mno = 'MNO'
pqrs = 'PQRS'
tuv = 'TUV'
wxyz = 'WXYZ'

for i in b:
    if i in abc:
        c = 3
        list.append(c)
    elif i in deF:
        c = 4
        list.append(c)
    elif i in ghi:
        c = 5
        list.append(c)
    elif i in jkl:
        c = 6
        list.append(c)
    elif i in mno:
        c = 7
        list.append(c)
    elif i in pqrs:
        c = 8
        list.append(c)
    elif i in tuv:
        c = 9
        list.append(c)
    elif i in wxyz:
        c = 10
        list.append(c)

print(sum(list))
