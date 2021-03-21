def data_file():
    with open('10_jolt.txt', 'r') as file:
        line = file.read()
        data = line.split('\n')
        for ind, dat in enumerate(data):
            dat = int(dat)
            data[ind] = dat
    data.sort()
    return data


def adapters(array):
    oneList = []
    threeList = []
    counter = 0
    for arr in array:
        if counter + 1 == arr:
            oneList.append(arr)
            counter += 1
        elif counter + 3 == arr:
            threeList.append(arr)
            counter += 3
        elif counter + 2 == arr or (counter + 3 > arr or counter - 3 < arr):
            print("error")
            break
    return len(oneList), len(threeList)


def adapter3(array):
    array.append(array[-1] + 3)
    counter = {0: 1}
    for i in array:
        counter[i] = counter.get(i - 3, 0) + counter.get(i - 2, 0) + counter.get(i - 1, 0)
    return counter[array[-1]]


print(data_file())
print(adapters2(data_file())[0])
print(adapters2(data_file())[1])
print(adapter3(data_file()))
