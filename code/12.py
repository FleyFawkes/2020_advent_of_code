def data_file():
    with open('12_route.txt', "r") as file_input:
        lines = file_input.read().splitlines()
    return lines


def chart(array):
    course = {"N": 0, "S": 0, "E": 0, "W": 0, "F": "E"}
    test = ["L", "R"]
    for arr in array:
        dire = arr[0]
        num = arr[1:]
        if dire in course:
            course[dire] += num
        if dire in test:
            course["F"] = angle(num, dire)
    north, south, east, west = course.get("N"), course.get("S"), course.get("E"), course.get("W")
    charted =


def angle(rotation, change):
    angle = ["E", "S", "W", "N"]
    arit = rotation // 90
    if change == "R":
        for ind in range(0, arit):
            x = angle.pop(0)
            angle.insert(-1, x)
    if change == "L":
        for ind in range(0, arit):
            x = angle.pop()
            angle.insert(0, x)
    return angle[0]
