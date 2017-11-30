#!/bin/bash

sudo yum -y install curl gcc make dnf install zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel xz xz-devel > /dev/null/ 2 > &1
sudo yum -y install git > /dev/null/ 2 > &1
cd ~/
curl -L https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash > /dev/null/ 2 > &1
export PATH="~/.pyenv/bin:$PATH" >> ~/.bash_profile
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
export PATH="~/.pyenv/bin:$PATH"
pyenv install 2.7.14 > /dev/null/ 2 > &1
pyenv install 3.6.3 > /dev/null/ 2 > &1
pyenv virtualenv 2.7.14 python2 | grep -Po '(?<=New python executable in ).+'
pyenv virtualenv 3.6.3 python3 | grep -Po '(?<=New python executable in ).+'






