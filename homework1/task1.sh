#!/bin/sh

yum update

yum install curl git-core gcc make zlib1g-dev libbz2-dev libreadline-dev \
libsqlite3-dev libssl-dev zlib-devel bzip2 bzip2-devel readline-devel \
sqlite sqlite-devel openssl-devel xz xz-devel

cd ~
sudo curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash

export PYENV_ROOT="$HOME/.pyenv”
export PATH="$PYENV_ROOT/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile

pyenv update

pyenv install 3.5.4
pyenv install 2.7.14
pyenv global 3.5.4

git config --global user.name "dzmitrytarasevich"
git config --global user.email "dmitrytarasevich@mail.ru"

pip install python-virtualenv

mkdir ~/projects
cd ~/projects

virtualenv -p python3 python3.5.4
virtualenv -p python2 python2.7.14

