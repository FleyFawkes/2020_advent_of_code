from math import gcd


def data_file():
    with open('13_bus.txt', "r") as file_input:
        lines = file_input.read().splitlines()
        lines = lines[1].split(',')
        line2 = []
        line1 = []
        tmp = 0
        for line in lines:
            if line == 'x':
                tmp += 1
            else:
                line2.append(tmp)
                tmp = 0
                line = int(line)
                line1.append(line)
        tmp = 0
        line22 = []
        for line in line2:
            tmp += line
            line22.append(tmp)
        del line2, lines
    return line1, line22


def divider(array):
    cd = array[0]
    for i in array[1:]:
        cd = cd * i // gcd(cd, i)
    return cd


def yellow(array, array1):
    time = 0
    number = [array[0]]
    while True:
        time += divider(number)
        for i, arr in enumerate(array):
            if (time + i + array1[i]) % arr == 0:
                if arr not in number:
                    number.append(arr)
        if len(number) == len(array):
            break
    return time


## brute force it:
#
# def timestamp(array, array2):
#     step = []
#     for _ in range(0, len(array)):
#         step.append(_)
#     for number in range(1068780, 1000000000000001):
#         var = 0
#         i = 0
#         j = 0
#         k = 0
#         while i < len(array):
#             arr = int(array[i])
#             numb = number + array2[j] + step[k]
#             if numb % arr == 0:
#                 var += 1
#                 if i == len(array) - 1:
#                     if numb % 100000 == 0:
#                         print(numb, var)
#                     if var == len(array) and numb % array[0] == 0:
#                         return number
#             i += 1
#             j += 1
#             k += 1


stop = yellow(data_file()[0], data_file()[1])
print(stop)
