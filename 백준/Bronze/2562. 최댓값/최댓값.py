list = []
for i in range(9):
    a = int(input())
    list.append(a)

max_num = max(list)
max_index = list.index(max_num) +1

print(max_num)
print(max_index)