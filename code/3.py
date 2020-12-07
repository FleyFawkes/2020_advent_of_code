file = open('3_map.txt', 'r')
lines = file.readlines()
file.close()
a = []
for line in lines:
    b = line.strip()
    a.append(b)


def limitmax(dictionary):
    if 'value' not in dictionary:
        dictionary.setdefault('value', 3)
    if dictionary['value'] > 30:
        dictionary['value'] = dictionary['value'] - 31
    return dictionary


def trees():
    number = numb + 1
    if number >= 323:
        number = 322
    output = a[number][limiter['value']]
    return output, number


numb = 0
tree = 0
dict = {}

while numb <= 322:
    for index, t in enumerate(a[numb]):
        limiter = limitmax(dict)
        if index == limiter['value']:
            treees = trees()
            if '#' in treees[0]:
                tree += 1
            a_list = treees[0]
            b_str = a[treees[1]]
            b_list = list(b_str)
            if a_list == '.':
                b_list[index] = 'O'
            if a_list == '#':
                b_list[index] = 'X'
            print(''.join(b_list))
            limiter['value'] += 3
            numb += 1
            break

print(tree)
