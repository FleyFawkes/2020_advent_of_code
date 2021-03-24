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
        test = ["L", "."]
        tested = [array[row][col - 1] in test,
                  array[row][col + 1] in test,
                  array[row - 1][col - 1] in test,
                  array[row - 1][col + 1] in test,
                  array[row - 1][col] in test,
                  array[row + 1][col] in test,
                  array[row + 1][col + 1] in test,
                  array[row + 1][col - 1] in test]
        if all(tested):
            return True
    elif array[row][col] == "#":
        var = 0
        if array[row][col - 1] == "#":
            var += 1
        if array[row][col + 1] == "#":
            var += 1
        if array[row - 1][col - 1] == "#":
            var += 1
        if array[row - 1][col + 1] == "#":
            var += 1
        if array[row - 1][col] == "#":
            var += 1
        if array[row + 1][col] == "#":
            var += 1
        if array[row + 1][col + 1] == "#":
            var += 1
        if array[row + 1][col - 1] == "#":
            var += 1
        if var > 3:
            return True
    else:
        return False


ferry = changeIntoList(addMargin(data_file()))
ferry = seatModel1(ferry)
ferry = delMargin(ferry)
a = 0
for fer in ferry:
    a += fer.count("#")

print(a)

