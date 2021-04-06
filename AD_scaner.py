
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      atopolskiy
#
# Created:     20.03.2021
# Copyright:   (c) atopolskiy 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import getpass
import keyring

from ldap3 import Server, Connection, ALL, SUBTREE, NTLM

AD_SEARCH_TREE = 'OU=Finam,OU=Users,OU=FMS,DC=office,DC=finam,DC=ru'


def write_file(name, mobile):
    '''
    Write new information into file
    We can use this file for search data
    '''

    with open('telephons.txt', 'a', encoding='utf-8') as file:
        file.write('\n'+ str(name) + '; ' + str(mobile))


def find_user_ad(sname):
    '''
    Initialize Server and connection
    Connect to server and search person with name {$cname}
    Take {$attr} from result
    '''

    systemname = 'office'
    username = 'office\atopolskiy-a'
    # Get from keyring password
    passwd = keyring.get_password(systemname, username)

    server = Server('msa-madr01-dc03', get_info=ALL)
    conn = Connection(server, user="office\\atopolskiy-a",
            password=passwd,
            authentication=NTLM)

    # establish connection without performing any bind (equivalent to ANONYMOUS bind)
    conn.bind()
    attr = ['displayName', 'mobile', 'mail']
    search_base = '(&(objectClass=person)(name=' + sname + '*))'

    srch=conn.search(AD_SEARCH_TREE, search_base, attributes=attr)

    if srch:    #If we  finded out search_base = True
        for entry in conn.entries:
            name = entry.displayName.value
            # write into file
            write_file(name, entry.mobile)
            print(name, entry.mobile)


def find_user_file(sname):
    '''
    Trying to find user($sname) into fiРеle ($file_name)
    '''
    sname = sname.lower()
    find_user = False
    file_name = 'telephons.txt'
    with open (file_name, 'r', encoding='utf-8') as file:
        for line in file:
            l = line.lower()
            if l.find(sname)>=0:
                print (line)
                find_user = True

    file.close()
    return find_user


def main():
    sname = input("Кого ищем?")
    find_user = False

    find_user = find_user_file(sname)
    if not find_user:
        find_user_ad(sname)



##    w = conn.extend.standard.who_am_i()

##    print(server.info)

if __name__ == '__main__':
    main()
