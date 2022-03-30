import subprocess as sb



sb.run('''sudo apt-get --purge remove build-essential linux-headers-$(uname -r) bison gawk python-setproctitle libreadline-gplv2-dev ledit gcc g++ zlibc 
 && sudo apt-get --purge remove zlib1g-dev
 && sudo apt-get --purge remove libreadline-dev
 && sudo apt autoremove''', shell=True, stdin=None, stdout=None, stderr=None, executable="/bin/bash")
 

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-Downloading Fonts-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

sb.run("""sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list' &&
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add - &&
sudo apt-get update &&
sudo apt-get -y install postgresql""", shell=True, stdin=None, stdout=None, stderr=None, executable="/bin/bash")

quit()



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




