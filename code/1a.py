file = open('1_numbers.txt', 'r')
lines = file.readlines()
a = []
for line in lines:
    b = int(line.strip())
    a.append(b)

file.close()

for numb in a:
    numa = 0
    while numa <= 199:
        numb_2 = a[numa]
        numaa = 0
        while numaa <= 199:
            if numb + numb_2 + a[numaa] == 2020:
                number = numb * numb_2 * a[numaa]
            numaa += 1
        numa += 1

print(number)
