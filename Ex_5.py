
import requests
import xml.etree.ElementTree as ET
import datetime
import sys

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
response = requests.get(url)
data = response.content
tree = ET.fromstring(data)

date = tree.attrib
rate_date = date['Date']
rate_date = datetime.datetime.strptime(rate_date, "%d.%m.%Y").date()
print(f'Exchange rate at {rate_date}')

def currency_rates(argv):
    i = 0
    value = None
    result = sys.argv[1:]
    result = str(result[0]).upper()

    for code in tree.iter('CharCode'):
        if code.text == result:
            value = tree[i][4].text
            value = float(value.replace(',', '.'))
        i += 1
    print(f'Exchange rate of {result} is {value}')


if __name__ == '__main__':
    import sys
    exit(currency_rates(sys.argv))
