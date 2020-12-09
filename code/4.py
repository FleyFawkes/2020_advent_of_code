def datafile():
    file = open('4_passports.txt', 'r')
    lines = file.readlines()
    file.close()
    a = []
    for line in lines:
        b = line.strip().split()
        a.append(b)
    return a


def index_limit(number):
    if number > 1167:
        number = 1167
    return number


def passlist(number, number_3):
    while number <= 1167:
        if a[number]:
            for item in a[number]:
                d = item
                c[number_3].append(d)
            number += 1
        if not a[index_limit(number)]:
            number += 1
            number_3 += 1
            c.append([])
            if number == 1167:
                del c[-1]
    return c


def passdict(list):
    master_list = []
    for item in list:
        dictionary = {}
        for item_2 in item:
            item_2_value = item_2[4:]
            item_2_key = item_2[0:3]
            dictionary[f'{item_2_key}'] = item_2_value
        master_list.append(dictionary)
    return master_list


def validator(list_of_dictionary):
    true_count = 0
    for dictionary in list_of_dictionary:
        if (len(dictionary.keys()) == 8) or (len(dictionary.keys()) == 7 and 'cid' not in dictionary.keys()):
            true_count += 1
    return true_count


if __name__ == '__main__':
    a = datafile()
    number = 0
    number_3 = 0
    c = [[]]
    c = passlist(number, number_3)
    passports_list = passdict(c)
    valid_passports = validator(passports_list)
    print(c)
    print(passports_list)
    print(len(passports_list))
    print(valid_passports)
