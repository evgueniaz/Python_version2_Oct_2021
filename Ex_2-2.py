
import requests
import xml.etree.ElementTree as ET
from decimal import *

url = 'http://www.cbr.ru/scripts/XML_daily.asp'

"""Документ с курсами валют скачан с указанного сайта"""

tree = ET.parse(r'C:\Users\evgue\OneDrive\Документы\GeekBrains\Python\XML_daily.asp')
root = tree.getroot()

def currency_rates(currency_code):
    i = 0
    value = None
    for code in root.iter('CharCode'):
        if code.text == currency_code.upper():
            value = root[i][4].text
            value = Decimal(value.replace(',', '.'))

        i += 1

    print(f'Exchange rate of {currency_code} is {value}')


currency_rates('EUR')
currency_rates('USD')
currency_rates('STE')
currency_rates('mex')
currency_rates('cad')
currency_rates('dKk')

