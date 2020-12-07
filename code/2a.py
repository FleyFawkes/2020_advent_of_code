file = open('2_passwords.txt', 'r')
lines = file.readlines()
a = []
for line in lines:
    b = line.strip().split()
    a.append(b)

file.close()
numb = 0
while numb <= 999:
    a[numb][1] = a[numb][1].replace(':', '')
    a[numb][0] = a[numb][0].replace('-', ' ')
    a[numb][0] = a[numb][0].split()
    numa = a[numb][0].pop()
    numaa = a[numb][0].pop()
    a[numb].append(numa)
    a[numb].append(numaa)
    del a[numb][0]
    a[numb][2] = int(a[numb][2])
    a[numb][3] = int(a[numb][3])
    numb += 1

numb = 0
c = 0

while numb <= 999:
    index_3 = False
    index_2 = False
    numba = 0
    toenum = a[numb][1]
    for index, num in enumerate(toenum):
        index = index + 1
        if f'{a[numb][0]}' in num:
            if index == a[numb][3]:
                index_3 = True
            if index == a[numb][2]:
                index_2 = True
    if index_3 and index_2 is False:
        c += 1
    if index_2 and index_3 is False:
        c += 1
    numb += 1

print(a)
print(c)
