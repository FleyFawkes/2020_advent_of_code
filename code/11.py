def data_file():
    with open('11_ferry.txt', 'r') as file:
        line = file.read()
        data = line.split('\n')
    return data


def addMargin(array):
    i = 1
    string = str()
    while i <= 98:
        string += '.'
        i += 1
    for _, arr in enumerate(array):
        arr = "." + arr + "."
        array[_] = arr
    array.insert(0, string)
    array.insert(len(array), string)
    return array


def seatModel(array):
    for _, arr in enumerate(array):
        arr = arr.replace('L', '#')
        array[_] = arr
    return array


def isValid(array, row, col):
    ver = 0
    newArray = array.copy()
    #add in seatmodel method to chande the array into list of lists.

ferry = seatModel(addMargin(data_file()))
print(ferry)
