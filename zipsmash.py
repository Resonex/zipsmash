def run():
    '''
    MIT License

Copyright (c) 2022 MJi | DarkƤwn [github.com/c4ssif3r]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
    'pip install google-search'
    try:
        import time as t
        from colorama import Fore as f
        import sys, os
        import zipfile
        from random import choice
    except:
        print("\033[0;31m please run command \033[0;32m pip install -r requirements.txt !")
        t.sleep(1)
        sys.exit()

    black = "\033[0;30m"
    red = "\033[0;31m"
    green = "\033[0;32m"
    brown = "\033[0;33m"
    blue = "\033[0;34m"
    purple = "\033[0;35m"
    cyan = "\033[0;36m"
    l_gray = "\033[0;37m"
    dark_gray = "\033[1;30m"
    l_red = "\033[1;31m"
    l_green = "\033[1;32m"
    yellow = "\033[1;33m"
    l_blue = "\033[1;34m"
    l_purple = "\033[1;35m"
    l_cyan = "\033[1;36m"
    l_white = "\033[1;37m"
    faint = "\033[2m"
    italic = "\033[3m"
    underline = "\033[4m"
    blink = "\033[5m"
    nefative = "\033[7m"
    cross = "\033[9m"
    ended = "\033[0m"
    bold = "\033[1m"
    nbold = "\033[0m"
    white = f.WHITE

    bnr = ['''
                         ▒███████▒      ██     ██▓███
                         ▒ ▒ ▒ ▄▀░    ▒▓██    ▓██░  ██
                         ░ ▒ ▄▀▒░     ░▒██    ▓██░ ██▓▒
                           ▄▀▒   ░     ░██    ▒██▄█▓▒ ▒
                         ▒███████▒     ░██    ▒██▒ ░  ░
                         ░▒▒ ▓░▒░▒     ░▓     ▒▓▒░ ░  ░
                         ░ ▒ ▒ ░ ▒      ▒     ░▒ ░
                         ░ ░ ░ ░ ░      ▒     ░░
                           ░ ░          ░               ''', '''
                         ░▒█▀▀▀█░░░▀█▀░░░▒█▀▀█
                         ░░▄▄▄▀▀░░░▒█░░░░▒█▄▄█
                         ░▒█▄▄▄█░░░▄█▄░░░▒█░░░ ''']

    def r_bnr(bnr):
        return choice(bnr)

    print (f'{blink}{r_bnr(bnr)}{ended}', end='')
    t.sleep(2)
    print(f' {italic}From{ended} : ', end='')
    #create flush text [simple]
    print(f'{red}{bold}', end='', flush=True)
    print(f'{bold}W', end='', flush=True)
    t.sleep(0.5)
    print('e', end='', flush=True)
    t.sleep(0.7)
    print('b', end='', flush=True)
    t.sleep(0.4)
    print('E', end='', flush=True)
    t.sleep(0.1)
    print('x', end='', flush=True)
    t.sleep(0.2)
    print('p', end='', flush=True)
    t.sleep(0.3)
    print('l', end='', flush=True)
    t.sleep(0.4)
    print('o', end='', flush=True)
    t.sleep(0.5)
    print('i', end='', flush=True)
    t.sleep(1.5)
    print(f't{ended}', flush=True)
    nbold = "\033[0m" # Resonex cruze !
    t.sleep(1)
    print(f'{white}{nbold}')

    print (f'\n                   {bold}{f.GREEN}[{f.WHITE}ZIP{f.GREEN}]{f.WHITE}{f.RED} Z.I.P{f.WHITE}{bold} ZIP {bold}C{nbold}racker T00L !\n\n\n')
    t.sleep(3)




    while True:
        try:
            zipc = input(f'\n  {f.WHITE}[{f.CYAN}{bold}WebExploit{f.WHITE}{nbold}@{f.RED}Z.I.P/{bold}FILE[zip]{nbold}{f.WHITE} enter {bold}\'zipFile{nbold}\' [ex: /Desktop/mji.zip]:#{f.GREEN}{bold} ')
            print(f'{nbold}')

            if zipc:
                break
            else:
                input('please enter a zip file')
                continue

        except Exception as err_zipc:
            print(f'\n\n      {nbold}{f.WHITE}[{f.RED}{bold}ERROR{f.WHITE}{nbold}] {bold}ERROR -> {err_zipc}{nbold} EXITTING . . .')
            t.sleep(2)
 #           break
            sys.exit(0)
    while True:
        passwords = input(f'\n  {f.WHITE}[{f.CYAN}{bold}WebExploit{f.WHITE}{nbold}@{f.RED}Z.I.P/{bold}ZIP-CRACKER{nbold}{f.WHITE} enter \'Password LIST{nbold}\' [ex: /home/WebExploit/Desktop/ssh-passwords.txt]:#{f.GREEN}{bold} ')
        if passwords:
            try:
                passes = open(passwords, 'r').readlines()
               # passes.close()
                break
            except Exception as file_err:
                print (f'\n   {nbold}{f.WHITE}[{f.RED}{bold}ERROR{f.WHITE}{nbold}@{f.RED}RARC/{f.GREEN}Passwords{white}] {nbold}{f.CYAN} ERROR : \'{bold}{file_err}{nbold}\' \n')
                t.sleep(1)
                continue
        t.sleep(1)
    print(f'\n  {f.WHITE}[{f.GREEN}{bold}INFO{f.WHITE}{nbold}@{f.RED}Z.I.P/{bold}ZIP-CRACKER{nbold}{f.YELLOW} Loadind modules {bold}zip-cracker . . . !{nbold}]')
    t.sleep(3)
    try:
        zip_file = zipc
        zip_file = zipfile.ZipFile(zip_file)
    except Exception as g_err:
        print ('err :  %s' % g_err)
    for pwd_ in passes:
        pwd1 = pwd_.strip()
        try:
            zip_file.extractall(pwd=pwd1.encode())
            print (f'\n   {nbold}{f.WHITE}[{f.GREEN}{bold}CRACKER{f.WHITE}{nbold}@{f.RED}ZIP.C/{f.GREEN}Password-Found{white}] {nbold}{f.CYAN} \'{bold}{pwd_}{nbold}\' \n')
        except:
            print (f'\n   {nbold}{f.WHITE}[{f.RED}{bold}CRACKER{f.WHITE}{nbold}@{f.RED}ZIP.C/{f.YELLOW}Password-NotFound{white}] {nbold}{f.RED} \'{bold}{pwd_}{nbold}\' \n')
            continue
        else:
            print(f'{green}')
            print("[ZIP-C] Password found:", word.decode().strip())
            exit(0)
    print(f'{red}')
    print("[ZIP-C] Password not found, try another wordlist [password-lists].")






