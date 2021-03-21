def data_file():
    with open('8_instructions.txt', 'r') as file:
        line = file.read()
        data = line.split('\n')
    return data


# with open('8_instructions.txt', "r") as file_input:
#     lines = file_input.read().splitlines()


def hopping(instructions):
    global ACC
    index = []
    a = 0
    ACC = 0
    while a < len(instructions):
        if a in index:
            return False
        else:
            index.append(a)
            item, value = instructions[a].split(" ")
            value = int(value)
            if 'acc' == item:
                ACC += value
                a += 1
            elif 'jmp' == item:
                a += value
            elif 'nop' == item:
                a += 1
    return True


def change(i):
    instructions = lines.copy()
    check = instructions[i]
    if 'jmp' in check:
        check = check.replace('jmp', 'nop')
        instructions[i] = check
    elif 'nop' in check:
        check = check.replace('nop', 'jmp')
        instructions[i] = check
    return instructions


def part2(instructions):
    global swapped
    if hopping(instructions):
        print(ACC)
    else:
        i = 0
        while i < len(instructions):
            if i not in swapped:
                instructions = change(i)
                swapped.append(i)
                break
            i += 1
        part2(instructions)


if __name__ == "__main__":
    lines = data_file()
    # operation = {}
    # for index, line in enumerate(lines):
    #     operation[index + 1] = line
    swapped = []
    part2(lines)
