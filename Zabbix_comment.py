#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Shoblin
#
# Created:     03.07.2020
# Copyright:   (c) Shoblin 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from datetime import datetime

TEMPLATE_ZABBIX = '''----------
{day:02}.{month:02}.{year} {hour:02}:{mins:02} А.Топольский:
https://sd.finam.ru/browse/{td}{explain}
'''


def zabbix_comment():
    '''
    Form a comment for updates in zabbix
    '''

    td = input ("Введите ссылку на TD:")
    explain = ""
    answer = ""
    while answer.lower() != 'q':
        print(answer.lower())
        explain +="\n" + answer
        answer = input('Введите обьяснение. Для прекращения ввода обьяснения введите Q: ')

    comment_date = datetime.now()
    comment = TEMPLATE_ZABBIX.format(
        day = comment_date.day, month = comment_date.month, year = comment_date.year,
        hour = comment_date.hour, mins = comment_date.minute,
        td = td,
        explain = explain)

    print(comment)




def main():
    zabbix_comment()


if __name__ == '__main__':
    main()
