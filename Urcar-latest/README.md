## 2022.03.29
---

## Intro
Use Web3-python to initialize and create an unchangeable smart contract for each vehicle, retrieve the contract address according to the vehicle ID, and query the vehicle information.

## Env
- Ubuntu 20.04
- python 3.8
- [web3](https://web3py.readthedocs.io/en/stable/quickstart.html#test-provider)
- [py-solc-x](https://web3py.readthedocs.io/en/stable/contracts.html)
- apache2
- wsgi
- requirements.txt

---

### 1. 部署地址

[在这里访问](http://120.78.228.15/)

### 2. 如何使用 apache2 和 wdgi 部署 dash app

https://github.com/fox000002/blog/blob/master/Install-Python-Dash-App-on-Ubuntu-Server.md
https://blog.csdn.net/qq_37430374/article/details/104249340


### 3. 配置过程记录

```
sudo add-apt-repository ppa:deadsnakes/ppa

sudo apt-get install mysql-client mysql-server

sudo apt-get install python3.8 python3.8-dev

sudo apt-get install apache2 apache2-dev

curl https://bootstrap.pypa.io/get-pip.py | sudo python3.8

sudo pip3.8 install mod_wsgi

mod_wsgi-express module-config
```
```
LoadModule wsgi_module "/usr/local/lib/python3.8/dist-packages/mod_wsgi/server/mod_wsgi-py38.cpython-38-x86_64-linux-gnu.so"
WSGIPythonHome "/usr"
```
```
sudo vim /etc/apache2/mods-available/wsgi.load

sudo pip3.8 install dash dash_bootstrap_components pandas 

sudo vim /etc/apache2/sites-available/FlaskApp.conf
```
```
<VirtualHost *:80>
   ServerName 120.78.228.15
   ServerAdmin zhongyuanguo@foxmail.com
   WSGIScriptAlias / /var/www/FlaskApp/FlaskApp.wsgi
   <Directory /var/www/FlaskApp/FlaskApp/>
        Order allow,deny
        Allow from all
   </Directory>
   ErrorLog ${APACHE_LOG_DIR}/FlaskApp-error.log
   LogLevel warn
   CustomLog ${APACHE_LOG_DIR}/FlaskApp-access.log combined
</VirtualHost>
```
```
sudo a2ensite FlaskApp

sudo vim /var/www/FlaskApp/FlaskApp.wsgi
```
```
#!/usr/bin/python3.8
# 测试用例，__init__.py
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/FlaskApp/FlaskApp/")
from FlaskApp.app import app
application = app.server
```

### 4. 怎样debug

每次改完py之后
`service apache2 reload`

如果网页显示不成功，在这里查看报错信息
`cd /var/log/apache2`
`vim FlaskApp-error.log`

### 5. TODO

1. `mkdir /var/www/.solcx`， 但是 web3 仍未获得权限
2. 添加进 FlaskApp.wsgi，无效
```
from solcx import install_solc
install_solc(version='latest')
```