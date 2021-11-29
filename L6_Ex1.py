

import re
from collections import Counter
from pprint import pprint

log_file = r"C:\Users\evgue\PycharmProjects\Geek_Python_2\Lesson_6\nginx_logs.txt"
regex_1 = r'(^\d+\.\d+\.\d+\.\d+)|(^((^|:)([0-9a-fA-F]{0,4})){1,8})'

match_list = []

with open(log_file, "r", encoding='utf-8') as f:
    for line in f:
        match_1 = re.search(regex_1, line)
        result = match_1.group()
        match_list.append(result)

# pprint(match_list)

spam_count = Counter(match_list).most_common(1)
print(f'IP of a spamer and amount of requests: {spam_count}')