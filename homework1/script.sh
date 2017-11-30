#!/bin/sh

curl -L https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
export PATH="/home/student/.pyenv/bin:$PATH"
pyenv install -l
sudo yum -y install patch sqlite-devel bzip2-devel readline-devel zlib-devel openssl-devel

pyenv install 3.5.0
pyenv install 2.7

pyenv local 3.5.0
pyenv global 3.5.0

export PATH="/home/student/.pyenv/versions/3.5.0/bin:$PATH"

pip install virtualenv

mkdir venv2.7
mkdir venv3.5

git add venv3.5 && echo “/venv3.5/” >> .gitignore && git add -f .
virtualenv --no-site-packages --prompt="(project3.5)" venv3.5

export PATH="/home/student/.pyenv/versions/2.7/bin:$PATH"
pyenv local 2.7
pyenv global 2.7

git add venv2.7 && echo “/venv2.7/” >> .gitignore && git add -f .
virtualenv --no-site-packages --prompt="(project2.7)" venv2.7

