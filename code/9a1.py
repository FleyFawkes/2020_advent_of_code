def data_file():
    with open('9_port.txt', 'r') as file:
        line = file.read()
        data = line.split('\n')
        for _, dat in enumerate(data):
            dat = int(dat)
            data[_] = dat
    return data


def counter(array):
    i = 25
    while i < len(array):
        numb = array[i]
        passed = []
        count = 0
        for ind in array[i - 25:i]:
            count += 1
            b = i - (25 - count)
            for ind2 in array[b:i]:
                if ind != ind2:
                    if ind + ind2 == numb:
                        passed.append(True)
        if True not in passed:
            return array[i], i
        i += 1


def contSet(number, array):
    print(number)
    numbList = []
    for ind in range(0, 30):
        i = 0
        while i < len(array):
            if i - ind < 0:
                i = ind
            passed = []
            for ind1 in array[i - ind:i]:
                passed.append(ind1)
                counter = 0
                for ind2 in passed:
                    counter += ind2
                    if counter == number and counter != passed[0]:
                        passed.append(counter)
                        numbList.append(True)
            if True in numbList:
                passed.sort()
                return passed[0] + passed[-2]
            i += 1


port = contSet(counter(data_file())[0], data_file())
print(port)
