#!/bin/bash
echo ------ Dependencias

sudo apt-get install build-essential linux-headers-$(uname -r) bison gawk python-setproctitle libreadline-gplv2-dev ledit gcc g++ zlibc
sudo apt-get install zlib1g-dev
sudo apt-get install libreadline-dev

echo --- Fontes

wget https://ftp.postgresql.org/pub/source/v9.2.4/postgresql-9.2.4.tar.gz --no-check-certificate
tar -zxvf postgresql-9.2.4.tar.gz
cd postgresql-9.2.4
./configure --prefix=/usr/local/pgsql/
sudo make
sudo make install

echo =-=-==-=-=--------------------------------------------------------

sudo adduser postgres
sudo mkdir -p /usr/local/pgsql/data
sudo chown -R postgres.postgres /usr/local/pgsql
sudo su postgres
/usr/local/pgsql/bin/initdb -D /usr/local/pgsql/data && locale=pt_BR.UTF-8
rm /usr/local/pgsql/share/timezone/America/Sao_Paulo 
su h
cd /usr/local/pgsql/share/timezone/America/
sudo wget https://cliente.hospidata.com.br/downloads/api/Apps/Infraestrutura/Sao_Paulo --no-check-certificate

sudo nano /etc/systemd/system/postgresql.service

sudo chmod +x /etc/systemd/system/postgresql.service
systemctl daemon-reload
systemctl enable postgresql
systemctl start postgresql
