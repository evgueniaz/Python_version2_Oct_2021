
import requests
import xml.etree.ElementTree as ET
import datetime

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
response = requests.get(url)
data = response.content
tree = ET.fromstring(data)

date = tree.attrib
rate_date = date['Date']
rate_date = datetime.datetime.strptime(rate_date, "%d.%m.%Y").date()
print(f'Exchange rate at {rate_date}')

def currency_rates(currency_code):
    i = 0
    value = None
    for code in tree.iter('CharCode'):
        if code.text == currency_code.upper():
            value = tree[i][4].text
            value = float(value.replace(',', '.'))
        i += 1
    print(f'Exchange rate of {currency_code} is {value}')

if __name__ == '__main__':
    currency_rates('USD')
    currency_rates('EUR')
    currency_rates('STE')
    currency_rates('mex')
    currency_rates('cad')
    currency_rates('dKk')

