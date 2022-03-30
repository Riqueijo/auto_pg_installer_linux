import subprocess as sb

#sb.run('sudo apt-get --purge remove postgresql postgresql-*', shell=True, stdin=None, stdout=None, stderr=None, executable="/bin/bash")

sb.run('''sudo apt-get install wget ca-certificates && wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add - && sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list' && sudo apt-get update && sudo apt-get install postgresql-9.2''', shell=True, stdin=None, stdout=None, stderr=None, executable="/bin/bash")







quit()

##  criando usuario

sb.run('sudo adduser postgres && sudo mkdir -p /usr/local/pgsql/data && sudo chown -R postgres.postgres /usr/local/pgsql', shell=True, stdin=None, stdout=None, stderr=None, executable="/bin/bash")
sb.run('usermod -aG sudo postgres', shell=True, stdin=None, stdout=None, stderr=None, executable="/bin/bash")
#log as new user and create db

sb.run('su postgres && sudo /usr/local/pgsql/bin/initdb -D /usr/local/pgsql/data --locale=pt_BR.UTF-8 && sudo rm /usr/local/pgsql/share/timezone/America/Sao_Paulo', shell=True, stdin=None, stdout=None, stderr=None, executable="/bin/bash")

#maaaaaaaaaaais configuracao

sb.run('sudo wget cliente.hospidata.com.br/downloads/api/Apps/Infraestrutura/Sao_Paulo', shell=True, stdin=None, stdout=None, stderr=None, executable="/bin/bash")

#iniciar banco

sb.run('/usr/local/pgsql/bin/pg_ctl -D /usr/local/pgsql/data start', shell=True, stdin=None, stdout=None, stderr=None, executable="/bin/bash")
