def data_file():
    with open('13_bus.txt', "r") as file_input:
        lines = file_input.read().splitlines()
        test = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        tmp = ""
        for _, line in enumerate(lines[1]):
            if line in test:
                tmp += line
                if _ + 1 == len(lines[1]):
                    lines.append(tmp)
            else:
                lines.append(tmp)
                tmp = ""
                if "" in lines:
                    lines.remove("")
        del lines[1]
    return lines


def depart(array):
    numbers = []
    numbers2 = []
    for arr in array[1:]:
        num = int(array[0])
        arr = int(arr)
        numb = num % arr
        numb2 = num - numb
        numb3 = numb2 + arr
        numbers.append(numb3)
        numbers2.append(arr)
    for _, arr in enumerate(numbers):
        num = arr - int(array[0])
        numbers.insert(_, num)
        numbers.pop(_ + 1)
    num = numbers[0]
    for arr in numbers:
        if arr < num:
            num = arr
    return num * numbers2[numbers.index(num)]


bus = depart(data_file())
print(bus)
