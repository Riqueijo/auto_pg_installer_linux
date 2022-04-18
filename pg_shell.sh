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

echo =-=-==-=-=-

adduser postgres
sudo mkdir -p /usr/local/pgsql/data
sudo chown -R postgres.postgres /usr/local/pgsql
sudo su postgres
/usr/local/pgsql/bin/initdb -D /usr/local/pgsql/data -- locale=pt
