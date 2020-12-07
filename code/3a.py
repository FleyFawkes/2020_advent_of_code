file = open('3_map.txt', 'r')
lines = file.readlines()
file.close()
a = []
for line in lines:
    b = line.strip()
    a.append(b)


def limitmax(dictionary, run):
    if 'value' not in dictionary:
        dictionary.setdefault('value', run)
    if dictionary['value'] > 30:
        dictionary['value'] = dictionary['value'] - 31
    return dictionary


def trees(numb, limiter, rundown):
    number = numb + rundown
    if number >= 323:
        number = 322
    output = a[number][limiter['value']]
    return output, number


def run_r3_d1():
    numb = 0
    run = 3
    tree = 0
    dict = {}
    while numb <= 322-1:
        for index, t in enumerate(a[numb]):
            limiter = limitmax(dict, run)
            if index == limiter['value']:
                treees = trees(numb, limiter, 1)
                if '#' in treees[0]:
                    tree += 1
                a_list = treees[0]
                b_str = a[treees[1]]
                b_list = list(b_str)
                if a_list == '.':
                    b_list[index] = 'O'
                if a_list == '#':
                    b_list[index] = 'X'
                #print(''.join(b_list))
                limiter['value'] += run
                numb += 1
                break
    return tree


def run_r1_d1():
    numb = 0
    run = 1
    tree = 0
    dict = {}
    while numb <= 322-1:
        for index, t in enumerate(a[numb]):
            limiter = limitmax(dict, run)
            if index == limiter['value']:
                treees = trees(numb, limiter, 1)
                if '#' in treees[0]:
                    tree += 1
                a_list = treees[0]
                b_str = a[treees[1]]
                b_list = list(b_str)
                if a_list == '.':
                    b_list[index] = 'O'
                if a_list == '#':
                    b_list[index] = 'X'
                #print(''.join(b_list))
                limiter['value'] += run
                numb += 1
                break
    return tree


def run_r5_d1():
    numb = 0
    run = 5
    tree = 0
    dict = {}
    while numb <= 322-1:
        for index, t in enumerate(a[numb]):
            limiter = limitmax(dict, run)
            if index == limiter['value']:
                treees = trees(numb, limiter, 1)
                if '#' in treees[0]:
                    tree += 1
                a_list = treees[0]
                b_str = a[treees[1]]
                b_list = list(b_str)
                if a_list == '.':
                    b_list[index] = 'O'
                if a_list == '#':
                    b_list[index] = 'X'
                #print(''.join(b_list))
                limiter['value'] += run
                numb += 1
                break
    return tree


def run_r7_d1():
    numb = 0
    run = 7
    tree = 0
    dict = {}
    while numb <= 322-1:
        for index, t in enumerate(a[numb]):
            limiter = limitmax(dict, run)
            if index == limiter['value']:
                treees = trees(numb, limiter, 1)
                if '#' in treees[0]:
                    tree += 1
                a_list = treees[0]
                b_str = a[treees[1]]
                b_list = list(b_str)
                if a_list == '.':
                    b_list[index] = 'O'
                if a_list == '#':
                    b_list[index] = 'X'
                #print(''.join(b_list))
                limiter['value'] += run
                numb += 1
                break
    return tree


def run_r1_d2():
    numb = 0
    run = 1
    tree = 0
    dict = {}
    while numb <= 322-2:
        for index, t in enumerate(a[numb]):
            limiter = limitmax(dict, run)
            if index == limiter['value']:
                treees = trees(numb, limiter, 2)
                if '#' in treees[0]:
                    tree += 1
                a_list = treees[0]
                b_str = a[treees[1]]
                b_list = list(b_str)
                if a_list == '.':
                    b_list[index] = 'O'
                if a_list == '#':
                    b_list[index] = 'X'
                #print(''.join(b_list))
                limiter['value'] += run
                numb += 2
                break
    return tree


if __name__ == '__main__':
    number_trees = run_r1_d2() * run_r3_d1() * run_r5_d1() * run_r7_d1() * run_r1_d1()
    print(number_trees)
