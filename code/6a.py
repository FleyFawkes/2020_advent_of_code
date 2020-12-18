def datafile():
    file = open('6_answers.txt', 'r')
    lines = file.readlines()
    file.close()
    a = []
    for line in lines:
        b = line.strip()
        a.append(b)
    return a


def grouping(list):
    listo = [[]]
    number = 0
    number_2 = 0
    while number <= 2240:
        if list[number]:
            listo[number_2].append(list[number])
            number += 1
        if not list[index_limit(number, 2240)]:
            number += 1
            number_2 += 1
            listo.append([])
    return listo


def index_limit(number, number_2):
    if number > number_2:
        number = number_2
    return number


def answ_list(list_a):
    number = 0
    number_3 = 0
    c = [[]]
    d = [[]]
    number_4 = 0
    while number <= 2240:
        if list_a[number]:
            c[number_3].append(list_a[number])
            number += 1
        if not list_a[index_limit(number, 2240)]:
            c[number_3].append(list_a[number])
            number += 1
            number_3 += 1
            c.append([])
            if number == 2240:
                del c[-1]
    for item in c:
        for item_2 in item:
            for item_3 in item_2:
                d[number_4].append(item_3)
            number_4 += 1
            d.append([])
    del d[-1]
    return d


def count_set(list):
    count = 0
    the_list = []
    for item in list:
        set_of_set = set()
        set_truth = True
        for item_2 in item:
            if bool(set_of_set) is False:
                set_of_set.update(item_2)
            elif bool(set_of_set):
                set_of_item = set()
                set_of_item.update(item_2)
                set_of_set = set_of_set.intersection(set_of_item)
                if bool(set_of_set) is False:
                    set_truth = False
        if set_truth is False:
            set_of_set = set()
        the_list.append(set_of_set)
        count += len(set_of_set)
    return count, the_list


if __name__ == '__main__':
    a = datafile()
    second = answ_list(a)
    third = grouping(second)
    fourth = count_set(third)
    print(fourth[0])
