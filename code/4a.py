import re
# it gives wrong answer by 2 entries. I don't know why.

def datafile():
    file = open('4_passports.txt', 'r')
    lines = file.readlines()
    file.close()
    a = []
    for line in lines:
        b = line.strip().split()
        a.append(b)
    return a


def index_limit(numb):
    if numb > 1167:
        numb = 1167
    return numb


def passlist(numb, numb_3, listo):
    while numb <= 1167:
        if listo[numb]:
            for item in listo[numb]:
                d = item
                c[numb_3].append(d)
            numb += 1
        if not listo[index_limit(numb)]:
            numb += 1
            numb_3 += 1
            c.append([])
            if numb == 1167:
                del c[-1]
    return c


def passdict(listo):
    master_list = []
    for item in listo:
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
        valid_count = 0
        for key, value in dictionary.items():
            if key == 'byr' and 1920 <= int(value) <= 2002:
                valid_count += 1
            elif key == 'iyr' and 2010 <= int(value) <= 2020:
                valid_count += 1
            elif key == 'eyr' and 2020 <= int(value) <= 2030:
                valid_count += 1
            elif key == 'hgt':
                if value[3:] == 'cm' and 150 <= int(value[0:3]) <= 193:
                    valid_count += 1
                elif value[2:] == 'in' and 59 <= int(value[0:2]) <= 76:
                    valid_count += 1
            elif key == 'ecl' and (value == 'amb' or 'blu' or 'brn' or 'gry' or 'grn' or 'hzl' or 'oth'):
                valid_count += 1
            elif key == 'pid':
                match = re.fullmatch(r'[0-9]{9}$', value)
                if match:
                    valid_count += 1
            elif key == 'hcl':
                match_2 = re.fullmatch(r'#[0-9a-f]{6}', value)
                if match_2:
                    valid_count += 1
        if valid_count == 7:
            true_count += 1
    return true_count


if __name__ == '__main__':
    adat = datafile()
    number = 0
    number_3 = 0
    c = [[]]
    c = passlist(number, number_3, adat)
    passports_list = passdict(c)
    valid_passports = validator(passports_list)
    print(valid_passports)
