import subprocess as sb

sb.run('''sudo apt-get --purge remove build-essential linux-headers-$(uname -r) bison gawk python-setproctitle libreadline-gplv2-dev ledit gcc g++ zlibc 
 && sudo apt-get --purge remove zlib1g-dev
 && sudo apt-get --purge remove libreadline-dev
 && sudo apt autoremove''', shell=True, stdin=None, stdout=None, stderr=None, executable="/bin/bash")


print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-Downloading Dependencies-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
sb.run('sudo apt-get install build-essential linux-headers-$(uname -r) bison gawk python-setproctitle libreadline-gplv2-dev ledit gcc g++ zlibc', shell=True, stdin=None, stdout=None, stderr=None, executable="/bin/bash")
            
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-ZLIB')
sb.run('sudo apt-get install zlib1g-dev', shell=True, stdin=None, stdout=None, stderr=None, executable="/bin/bash")

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-LIBREAD')
sb.run('sudo apt-get install libreadline-dev', shell=True, stdin=None, stdout=None, stderr=None, executable="/bin/bash")



print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-Downloading Fonts-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
sb.run('sudo wget https://ftp.postgresql.org/pub/source/v9.2.4/postgresql-9.2.4.tar.gz', shell=True, stdin=None, stdout=None, stderr=None, executable="/bin/bash")
sb.run('tar -zxvf postgresql-9.2.4.tar.gz', shell=True, stdin=None, stdout=None, stderr=None, executable="/bin/bash")

def param():
    ask = str(input('''parametrize os seguintes arquivos? postgresql.conf e pg_hba.conf
    [1] Feito.'''))
    if ask == 1:
        pass

quit()



