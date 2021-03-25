def data_file():
    with open('12_route.txt', "r") as file_input:
        lines = file_input.read().splitlines()
    return lines


def chart(array):
    course = {"N": 0, "S": 0, "E": 0, "W": 0, "F": "E"}
    rose = ["E", "S", "W", "N"]
    test = ["L", "R"]
    for arr in array:
        dire = arr[0]
        num = int(arr[1:])
        if dire in course:
            if dire == "F":
                course[course["F"]] += num
                continue
            course[dire] += num
        if dire in test:
            course["F"] = angleCalc(num, dire, rose)
    north, south, east, west = course.get("N"), course.get("S"), course.get("E"), course.get("W")
    ns = [north, south]
    ew = [east, west]
    ns.sort(reverse=True)
    ew.sort(reverse=True)
    ns = ns[0] - ns[1]
    ew = ew[0] - ew[1]
    return ns, ew


def angleCalc(rotation, change, angle):
    arit = rotation // 90
    if change == "R":
        for ind in range(0, arit):
            x = angle.pop(0)
            angle.append(x)
    if change == "L":
        for ind in range(0, arit):
            x = angle.pop()
            angle.insert(0, x)
    return angle[0]


routing = chart(data_file())
print(routing[0] + routing[1])
