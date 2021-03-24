import copy


def data_file():
    with open('11_ferry.txt', 'r') as file:
        line = file.read()
        data = line.split('\n')
    return data


def addMargin(array):
    i = 1
    string = str()
    while i <= len(array[0]) + 2:
        string += '.'
        i += 1
    for _, arr in enumerate(array):
        arr = "." + arr + "."
        array[_] = arr
    array.insert(0, string)
    array.insert(len(array), string)
    return array


def delMargin(array):
    newArray = []
    del array[-1]
    del array[0]
    for arr in array:
        del arr[0]
        del arr[-1]
    for arr in array:
        tmp = ""
        for arr2 in arr:
            tmp += arr2
        newArray.append(tmp)
    return newArray


def changeIntoList(array):
    newArray = []
    for arr in array:
        tmp = []
        for arr2 in arr:
            tmp.append(arr2)
        newArray.append(tmp)
    return newArray


def seatModel1(array):
    newArray = copy.deepcopy(array)
    i = 1
    while i < len(array) - 1:
        for ind, arr in enumerate(array[i]):
            if isValid(array, i, ind):
                newArray[i].pop(ind)
                if arr == "L":
                    newArray[i].insert(ind, "#")
                else:
                    newArray[i].insert(ind, "L")
        i += 1
    if newArray == array:
        return array
    else:
        return seatModel1(newArray)


def isValid(array, row, col):
    if array[row][col] == "L":
        var = 0
        a, b, c, d, e, f, g, h = True, True, True, True, True, True, True, True
        test = ["L", "#"]
        tested = []
        for num in range(1, 15):
            limit = instLimits(array, num, row, col)
            if (array[row][limit[3]] in test) and a:
                a = False
                var += 1
                tested.append(array[row][limit[3]])
            if (array[row][limit[2]] in test) and b:
                b = False
                var += 1
                tested.append(array[row][limit[2]])
            if (array[limit[1]][limit[3]] in test) and c:
                c = False
                var += 1
                tested.append(array[limit[1]][limit[3]])
            if (array[limit[1]][limit[2]] in test) and d:
                d = False
                var += 1
                tested.append(array[limit[1]][limit[2]])
            if (array[limit[1]][col] in test) and e:
                e = False
                var += 1
                tested.append(array[limit[1]][col])
            if (array[limit[0]][col] in test) and f:
                f = False
                var += 1
                tested.append(array[limit[0]][col])
            if (array[limit[0]][limit[2]] in test) and g:
                g = False
                var += 1
                tested.append(array[limit[0]][limit[2]])
            if (array[limit[0]][limit[3]] in test) and h:
                h = False
                var += 1
                tested.append(array[limit[0]][limit[3]])
            if "#" in tested:
                return False
            if var > 7:
                return True
            if num > 13:
                return True
    if array[row][col] == "#":
        var = 0
        test = ["#", "L"]
        tested = []
        a, b, c, d, e, f, g, h = True, True, True, True, True, True, True, True
        for num in range(1, 15):
            limit = instLimits(array, num, row, col)
            if (array[row][limit[3]] in test) and a:
                a = False
                var += 1
                tested.append(array[row][limit[3]])
            if (array[row][limit[2]] in test) and b:
                b = False
                var += 1
                tested.append(array[row][limit[2]])
            if (array[limit[1]][limit[3]] in test) and c:
                c = False
                var += 1
                tested.append(array[limit[1]][limit[3]])
            if (array[limit[1]][limit[2]] in test) and d:
                d = False
                var += 1
                tested.append(array[limit[1]][limit[2]])
            if (array[limit[1]][col] in test) and e:
                e = False
                var += 1
                tested.append(array[limit[1]][col])
            if (array[limit[0]][col] in test) and f:
                f = False
                var += 1
                tested.append(array[limit[0]][col])
            if (array[limit[0]][limit[2]] in test) and g:
                g = False
                var += 1
                tested.append(array[limit[0]][limit[2]])
            if (array[limit[0]][limit[3]] in test) and h:
                h = False
                var += 1
                tested.append(array[limit[0]][limit[3]])
            varstr = tested.count("L")
            for vast in range(1, varstr + 1):
                tested.remove("L")
            var = var - varstr
            if var > 4:
                return True
    else:
        return False


def instLimits(array, num, row, col):
    rowa = row + num
    rowb = row - num
    cola = col + num
    colb = col - num
    if rowa > len(array) - 1:
        rowa = len(array) - 1
    if rowb < 1:
        rowb = 0
    if cola > len(array[row]) - 1:
        cola = len(array[row]) - 1
    if colb < 1:
        colb = 0
    return rowa, rowb, cola, colb


ferry = changeIntoList(addMargin(data_file()))
ferry = seatModel1(ferry)
ferry = delMargin(ferry)
zero = 0
for fer in ferry:
    zero += fer.count("#")

print(ferry)
print(zero)
