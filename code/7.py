# import re
#
#
# def data_file():
#     with open('7_bags.txt', 'r') as file:
#         line = file.read()
#         data = line.split('\n')
#     return data
#
#
# def gold_search(listo):
#     for index, line in enumerate(listo):
#         match = re.search(r'.shiny gold', line)
#         if match:
#             gold_line.append(line)
#             gold_index.append(index + 1)
#     for line in gold_line:
#         match = re.match(r'[a-z]+\s[a-z]+', line)
#         if match:
#             gold_line_sorted.append(match.group(0))
#     return gold_line, gold_index, gold_line_sorted
#
#
# def gold_sorted(listo, gold_line_sorted):
#     count = 0
#     for line in gold_line_sorted:
#         for index, line_2 in enumerate(listo):
#             match = re.search(fr'.{line}', line_2)
#             if match:
#                 match_2 = re.match(r'[a-z]+\s[a-z]+', line_2)
#                 if match_2.group(0) in gold_line_sorted_2:
#                     count += 1
#                     continue
#                 else:
#                     gold_line_sorted_2.append(match_2.group(0))
#                     gold_index_2.append(index + 1)
#     if count < len(gold_line_sorted_2):
#         gold_sorted(listo, gold_line_sorted_2)
#     set_of_gold = set(gold_line_sorted_2)
#     set_of_gold_index = set(gold_index_2)
#     return set_of_gold, set_of_gold_index
#
#
# if __name__ == '__main__':
#     gold_line = []
#     gold_index = []
#     gold_line_sorted = []
#     gold_line_sorted_2 = []
#     gold_index_2 = []
#     a = data_file()
#     b = gold_search(a)
#     c = gold_sorted(a, b[2])
#     print(b[2])
#     print(c[0])
#     print(c[1])
#     print(len(c[1]))
