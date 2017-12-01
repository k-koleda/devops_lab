yum -y install gcc zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel tk-devel git
curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
pyenv install 2.7.14
pyenv install 3.5.4
pyenv versions
pyenv local 2.7.14
pyenv virtualenv 2.7.14 py2.7
pyenv local 3.5.4
pyenv virtualenv 3.5.4 py3.5
