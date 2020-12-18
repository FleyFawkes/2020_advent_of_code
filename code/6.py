def datafile():
    file = open('6_answers.txt', 'r')
    lines = file.readlines()
    file.close()
    a = []
    for line in lines:
        b = line.strip()
        a.append(b)
    return a


def answ_list(list_a):
    number = 0
    number_3 = 0
    c = [[]]
    while number <= 2240:
        if list_a[number]:
            for item in list_a[number]:
                d = item
                c[number_3].append(d)
            number += 1
        if not list_a[index_limit(number, 2240)]:
            number += 1
            number_3 += 1
            c.append([])
            if number == 2240:
                del c[-1]
    return c


def index_limit(number, number_2):
    if number > number_2:
        number = number_2
    return number


def uni_set(list):
    count = 0
    for item in list:
        set_of_set = set()
        set_of_set.update(item)
        count += len(set_of_set)
    return count


if __name__ == '__main__':
    a = datafile()
    c = answ_list(a)
    yes = uni_set(c)
    print(c)
    print(len(c))
    print(yes)
