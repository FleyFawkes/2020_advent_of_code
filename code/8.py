def data_file():
    with open('8_instructions.txt', 'r') as file:
        line = file.read()
        data = line.split('\n')
    return data


# with open('8_instructions.txt', "r") as file_input:
#     lines = file_input.read().splitlines()


lines = data_file()
operation = {}
items = []
for index, line in enumerate(lines):
    operation[index + 1] = line

a = 1
acc = 0
while True:
    item = operation[a]
    if a in items:
        print(acc)
        print(items)
        break
    items.append(a)
    if 'acc' in item:
        numb = item[4:]
        acc += int(numb)
        a += 1
    elif 'jmp' in item:
        numb = item[4:]
        a += int(numb)
    else:
        a += 1
