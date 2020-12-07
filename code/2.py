file = open('2_passwords.txt', 'r')
lines = file.readlines()
a = []
for line in lines:
    b = line.strip().split()
    a.append(b)

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
numba = 0

while numb <= 999:
    for num in a[numb][1]:
        if f'{a[numb][0]}' in num:
            numba += 1
    if a[numb][3] <= numba <= a[numb][2]:
        c += 1
    numba = 0
    numb += 1

print(c)
