# Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
# Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
# Убедиться, что ничего лишнего не происходит.

import utils

utils.currency_rates('cad')
utils.currency_rates('Inr')
utils.currency_rates('RON')
utils.currency_rates('HUN')