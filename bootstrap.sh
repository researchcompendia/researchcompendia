#!/usr/bin/env bash

# Warning: This script is completely in flux. Furthermore, all of the steps
# to deploy things are not automated by this script. Manual steps are 
# still required.
#
# This automates things according to suggestions from "Setting up Django with Nginx,
# Gunicorn, virtualenv, supervisor and PostgreSQL" but with a few differences.
# http://michal.karzynski.pl/blog/2013/06/09/django-nginx-gunicorn-virtualenv-supervisor/


apt-get update -y

apt-get install -y python-software-properties \
    python-dev \
    build-essential \
    python-pip \
    nginx \
    libxslt1-dev \
    supervisor \
    git \
    postgresql \
    postgresql-server-dev-9.1 \
    memcached \
    vim-nox \
    exuberant-ctags \
    multitail \
    curl \
    tmux \
    htop \
    memcached \
    libmemcached-dev \
    ack-grep

# get a more recent version of rabbitmq than is in the debian repo
wget http://www.rabbitmq.com/rabbitmq-signing-key-public.asc
sudo apt-key add rabbitmq-signing-key-public.asc
sudo add-apt-repository 'deb http://www.rabbitmq.com/debian/ testing main'
apt-get update -y
apt-get install -y rabbitmq-server

pip install virtualenvwrapper
pip install setproctitle # or just in a virtualenv?

# Lock things down a little
sed -i -e 's/# server_tokens off;/server_tokens off;/g' /etc/nginx/nginx.conf
sed -i -e 's/^#PasswordAuthentication yes/PasswordAuthentication no/g' /etc/ssh/sshd_config
echo DebianBanner no >> /etc/ssh/sshd_config
service ssh restart

useradd -s/bin/bash -d/home/tyler -m tyler
su postgres -c 'createuser -S -D -R -w tyler'
su postgres -c 'createdb -w -O tyler tyler'

# this isn't needed for debian wheezy since it already has this setting
#Add an entry to /etc/postgresql/9.1/main/pg_hba.conf,
#cat >> /etc/postgresql/9.1/main/pg_hba.conf <<\EOF
#local   all all        peer 
#EOF
#service postgresql restart

cat << 'NGINX' > /etc/nginx/sites-available/rehackable
upstream rehackable_org {
    server 127.0.0.1:8000;
}

server {
    listen 80;
    server_name rehackable.org;

    access_log /home/tyler/site/logs/tyler.access.log;
    error_log /home/tyler/site/logs/tyler.error.log;

    location /static/ {
        alias /home/tyler/site/static/;
    }
    location /media/ {
        alias /home/tyler/site/media/;
    }
    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_pass http://rehackable_org;
    }
}
NGINX
unlink /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/rehackable /etc/nginx/sites-enabled/

cat << 'SUPERVISOR' > /etc/supervisor/conf.d/tyler.conf
[program:tyler]
command = /home/tyler/site/bin/runserver.sh
user = tyler
stdout_logfile = /home/tyler/site/logs/gunicorn_supervisor.log
redirect_stderr = true
SUPERVISOR

cat << 'TYLER_BOOTSTRAP' > ~tyler/bootstrap.sh
#!/usr/bin/env bash

cd

cat << 'ALIASES' > .bash_aliases
if [ -f /usr/local/bin/virtualenvwrapper.sh ]; then
    . /usr/local/bin/virtualenvwrapper.sh
fi
export WORKON_HOME=${HOME}/venvs
ALIASES

source .bash_aliases

mkdir venvs
mkvirtualenv tyler
git clone https://gist.github.com/7583630.git
mkdir site
cd site
mkdir bin logs

echo export SECRET_KEY=\"`dd if=/dev/urandom bs=512 count=1 | tr -dc 'a-zA-Z0-9~@#%^&*-_'`\" >> bin/environment.sh

# TODO: need to work out how to get all of the env vars here
source bin/environment.sh

cp ~/7583630/runserver.sh bin/
chmod +x bin/runserver.sh
git clone git://github.com/researchcompendia/tyler.git
cd tyler

pip install -r requirements/production.txt
cd companionpages

# don't run these until we work out getting the env vars
# Warning: There is an issue that requires apps to be migrated explicitely
# versus calling ./manage.py migrate

#./manage.py syncdb --noinput
#./manage.py loaddata fixtures/*
#./manage.py migrate taggit
#./manage.py migrate users
#./manage.py migrate home
#./manage.py migrate compendia
#./manage.py migrate allauth.socialaccount
TYLER_BOOTSTRAP

cd ~tyler
su tyler -c 'bash ~/bootstrap.sh'

# don't run these until we work out getting the env vars
#supervisorctl reread
#supervisorctl update
# TODO: add a check to make sure everything started okay
