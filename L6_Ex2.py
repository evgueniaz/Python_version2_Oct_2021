

import re
from pprint import pprint

log_file = r"C:\Users\evgue\PycharmProjects\Geek_Python_2\Lesson_6\nginx_logs.txt"
regex_1 = r'(^\d+\.\d+\.\d+\.\d+)|(^((^|:)([0-9a-fA-F]{0,4})){1,8})'
regex_2 = r'(["]\w+)'
regex_3 = r'(/downloads/\w+)'

match_list = []

with open(log_file, "r", encoding='utf-8') as f:
    for line in f:
        match_1 = re.search(regex_1, line)
        match_2 = re.search(regex_2, line)
        # match_2 = re.sub(r'^"', '', match_2)
        match_3 = re.search(regex_3, line)
        result = (match_1.group(), match_2.group(), match_3.group())

        match_list.append(result)

pprint(match_list)

