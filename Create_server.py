#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      atopolskiy
#
# Created:     16.06.2020
# Copyright:   (c) atopolskiy 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
##import argparse

TEMPLATE_MENU = '{}. {}'

TRUE_ANS = ['yes', 'y', 'д', 'да']
FALSE_ANS = ['no', 'n', 'н', 'нет']
EXIT_ANS = ['exit', 'e']

def print_menu(menu_items):
    '''
    Create Menu using dictionary and display it
    '''
    print()
    for item in range(len(menu_items)):
        item = TEMPLATE_MENU.format(item + 1, menu_items[item + 1]['title'])
        print(item)


def print_rol_from_template():
    '''
    Print hosts and IS
    '''
    template_rol_name = "ROL-SRV-Admin_{}"
    template_is = "ROL-IS_{}"
    hosts = input('Введите именна созданых хостов через пробел: ')

    for host in hosts.split():
        host = host.upper()

        print(template_rol_name.format(host))

    is_num = input('ВВедите номер контура: ')
    print(template_is.format(is_num))


def oi_func(questions, result):
    ''''''
    for question in questions:
        bl_quest_ans = True
        while bl_quest_ans:
            bl_quest_ans = False

            print()
            print('=' * 40)
            print('Варианты ответов на вопросы:')
            print('YES  = ' + ','.join(TRUE_ANS))
            print('NO   = ' + ','.join(FALSE_ANS))
            print('EXIT = ' + ','.join(EXIT_ANS))
            print('=' * 40)

            ans = input(question['question'])
            ans = ans.lower()

            #Check: Does client want exit from
            if ans in EXIT_ANS:
                print(result)
                return None

            if ans in TRUE_ANS:
                result += question['answer']

                if question['print']:
                    print('\n#' * 15)
                    print('# ' + question['print'])
                    print('#' * 15 + '\n')

            if ans not in TRUE_ANS and ans not in FALSE_ANS:
                bl_quest_ans = True

    print(result)


def list_servers():
    '''Create list of servers from input date'''

    servers = input('Введите именна созданых хостов через пробел: ')
    return servers.split()

def text_num_servers():
    '''Count number of servers and then decide what phrase we need print'''

    servers = list_servers()

    if len(servers) == 1:
        result = 'Создан сервер {}\n'.format(servers[0])
        rols = 'Создана группа ROL-SRV-Admin_{} '.format(servers[0])
        mon = 'Сервер {} поставлен на мониторинг в Zabbix'.format(servers[0])
    elif len(servers) > 1:
        result = 'Созданы сервера: {}\n'.format(', '.join(servers))
        rols = 'Созданы группы:{}\n'.format(' ROL-SRV-Admin_'.join(servers))
        mon = 'Сервера {} поставлен на мониторинг в Zabbix\n'.format(', '.join(servers))

    return result, rols, mon


def check_list():
    '''
    ======================
    === Get check list ===
    ======================
    '''
    print ('\n' + '='*32)
    print ('Какой сервер вы хотите создать:')
    print ('='*32)
    print ('1. Windows Server')
    print ('2. Linux Server')
    print ('3. Linux Server Wt')

    creat_os = int(input('Введите номер от 1-3 '))

    if creat_os < 2:
        check_list_windows()
    elif creat_os >= 2 and creat_os <= 3:
        check_list_linux(creat_os)
    else:
        print('Нужно ввести чмсло от 1 до 3х')


def check_list_windows():
    '''
    ============================
    Print check list for Windows
    ============================
    '''

    result, rols, mon = text_num_servers()

    questions = [
    {'question':'Подключены дополнительных дисков? ', 'answer':'Подключены дополнительных диски\n', 'print': None},
    {'question':'Изменен файл подкачки на фиксированное значение в 2 Гб? ', 'answer':'Изменил файла подкачки на фиксированное значение в 2 Гб\n', 'print': None},
    {'question':'Отключен ли уязвимости протоколов, с помощью IISCrypto? ', 'answer':'Отключены уязвимости протоколов, с помощью IISCrypto\n', 'print': None},
    {'question':'Cозданы группы безопасности ROL-SRV-Admin_ИмяСервера? ', 'answer':rols, 'print': rols},
    {'question':'УЗ ВМ добавил в соответствующую группу SYS\SCCM? ', 'answer': 'УЗ ВМ добавил в соответствующую группу SYS\SCCM\n', 'print': None},
    {'question':'Добавлена в локальную группу Administrators ВМ группы безопасности ROL-SRV-Admin_ИМЯ_ВМ? ', 'answer': 'Добавлена в локальную группу Administrators ВМ группы безопасности\n', 'print': None},
    {'question':'Сервер поставлен на мониторинг Zabbix? ', 'answer': mon, 'print': None}
    ]

    oi_func(questions, result)


def check_list_linux(lnx):
    '''Print check list for Linux'''

    result, rols, mon = text_num_servers()
    if lnx == 2 :
        questions = [
        {'question':'Настроены сетевыйе интерфейсы, hostname, resolv.conf и timezone? ', 'answer':'Настроены сетевыйе интерфейсы, hostname, resolv.conf и timezone\n', 'print': None},
        {'question':'Выполнены Базовые настройки через систему централизованного конфигурирования Ansible? ', 'answer':'Базовые настройки через систему централизованного конфигурирования Ansible выполнены\n', 'print': None},
        {'question':'Cозданы группы безопасности ROL-SRV-Admin_ИмяСервера? ', 'answer':rols, 'print': rols},
        {'question':'Сервер поставлен на мониторинг Zabbix? ', 'answer': mon, 'print': None},
        {'question':'Установлен докер? ', 'answer': 'На сервере установлен докер через ansible', 'print': None},
        {'question':'Расширены диски? ', 'answer': 'На сервере расширены диски в соответствии с заявкой', 'print': None}
        ]
    elif lnx == 3:
        questions = [
        {'question':'Настроены сетевыйе интерфейсы, hostname, resolv.conf и timezone?', 'answer':'Настроены сетевыйе интерфейсы, hostname, resolv.conf и timezone\n', 'print': None}
        ]

    oi_func(questions, result)


def main():

    menu_items = {
    1: {'function': print_rol_from_template,
        'title': 'Помощь по созданию сервера'},
    2: {'function': check_list,
        'title': 'Чеклист по созданию сервера'},
    3: {'function': exit,
        'title': 'Выйти'}
    }


    print_menu(menu_items)
    while True:
        menu_item = input('Введите, что вы хотите: ')
        menu_items[int(menu_item)]['function']()



if __name__ == '__main__':
    main()
