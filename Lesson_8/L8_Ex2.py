# (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>,
#    <response_size>), например:
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')


import re
from pprint import pprint

log_file = r"C:\Users\evgue\PycharmProjects\Geek_Python_2\Lesson_6\nginx_logs.txt"
regex_1 = r'(^\d+\.\d+\.\d+\.\d+)|(^((^|:)([0-9a-fA-F]{0,4})){1,8})'
regex_2 = r'((?<=\[)\S+[ +]{2}[0-9]{4})'
regex_3 = r'((?<=")\w+)'
regex_4 = r'(/downloads/\w+)'
regex_5 = r'((?<=1\.1" )[0-9]{3})'
regex_6 = r'(([0-9]{1,8})(?= \"\-\"))|([0-9]{1,8})(?= \"http)'

match_list = []

with open(log_file, "r", encoding='utf-8') as f:
    for line in f:
        match_1 = re.search(regex_1, line)
        match_2 = re.search(regex_2, line)
        match_3 = re.search(regex_3, line)
        match_4 = re.search(regex_4, line)
        match_5 = re.search(regex_5, line)
        match_6 = re.search(regex_6, line)
        
        parsed_raw = (match_1.group(), match_2.group(), match_3.group(),
                      match_4.group(), match_5.group(), match_6.group())

        # match_list.append(result)
        print(parsed_raw)
pprint(match_list)
