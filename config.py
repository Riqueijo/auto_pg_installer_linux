import subprocess as sb



sb.run('cd postgresql-9.2.4 && ./configure --prefix=/usr/local/pgsql/ && make && make install', shell=True, stdin=None, stdout=None, stderr=None, executable="/bin/bash")

##  criando usuario

sb.run('sudo adduser postgres && sudo mkdir -p /usr/local/pgsql/data && sudo chown -R postgres.postgres /usr/local/pgsql', shell=True, stdin=None, stdout=None, stderr=None, executable="/bin/bash")
sb.run('usermod -aG sudo postgres', shell=True, stdin=None, stdout=None, stderr=None, executable="/bin/bash")
#log as new user and create db

sb.run('su postgres && sudo /usr/local/pgsql/bin/initdb -D /usr/local/pgsql/data --locale=pt_BR.UTF-8 && sudo rm /usr/local/pgsql/share/timezone/America/Sao_Paulo', shell=True, stdin=None, stdout=None, stderr=None, executable="/bin/bash")

#maaaaaaaaaaais configuracao

sb.run('sudo wget cliente.hospidata.com.br/downloads/api/Apps/Infraestrutura/Sao_Paulo', shell=True, stdin=None, stdout=None, stderr=None, executable="/bin/bash")

#iniciar banco

sb.run('/usr/local/pgsql/bin/pg_ctl -D /usr/local/pgsql/data start', shell=True, stdin=None, stdout=None, stderr=None, executable="/bin/bash")

