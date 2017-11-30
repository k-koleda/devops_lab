#!/bin/bash
sudo yum -y install curl git core gcc make zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel xz xz-devel python-virtualenv
sudo cat << EOF >> ~/.bash_profile
export PATH="/home/student/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
EOF
source ~/.bash_profile
curl -L https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
pyenv install 2.7
pyenv install 3.5.4
pyenv virtualenv venv2.7
pyenv activate venv2.7
pyenv global 2.7
pyenv deactivate
pyenv virtualenv venv3.5
pyenv activate venv3.5
pyenv global 3.5.4
pyenv deactivate
