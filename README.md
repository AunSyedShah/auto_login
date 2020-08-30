[![Open Source Love](https://github.com/umair313/auto_login/blob/readme/misc/open-source.svg)](https://github.com/umair313/auto_login/blob/readme/misc)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
![welcome](https://github.com/umair313/auto_login/blob/readme/misc/welcome.png)

# AUTO VU LMS LOGIN 

This tool is created for Vitual university students for auto login perpose 
currently working for chrome brower other browser will be added soon.

## Requirements 

#### *Download and install [Python 3](https://www.python.org/)*

#### *install [pip3](https://pypi.org/project/pip/)*

#### *install [Virtualenv](https://pypi.org/project/virtualenv/)*

#### *install [Selenium](https://selenium-python.readthedocs.io/)*

#### *install [requests](https://pypi.org/project/requests/)*

#### *Dwonload : [chrome Driver](https://chromedriver.chromium.org/)*

#### *Setup Driver : [Setup driver](https://chromedriver.chromium.org/)*

Now on we assume that you already have installed python on your systems
before going further check your python version <br>open **CMD** / **Terminal** type command:
````
python --version
````
if you have version < 3 then please upgrade it to python 3

### install pip
when you install python you also install pip its comes with python but if have lower<br> version then following command 
will install latet version of pip.
````
pip install pip
````

### install Virtualenv
````
pip install virtualenv
````

#### *now create a new Virtual Environment by using these command*
first we will create a empty directory you can name it what ever you like we are sying it **AutoLogin**
move to the new created Directory
create an Virtual Environment name it any name you like we are sying **base** 
activate it
#### Done

Right now my current directory is
````
D:\python\Project
````
#### Now lets do it

````
D:\python\project > mkdir AutoLogin

D:\python\project\AutoLogin > virtualenv base

D:\python\project > base\Scripts\activate

````
after this you wil see

````
(base) D:\python\project > 
````
now its activated and their will be two folders <br>
**base** that belongs to Virtual Environment
**Autologin** in this folder we will use our program files

#### Now install other **Dependences**.
move to AutoLogin Directory
````

D:\python\project > cd AutoLogin

D:\python\project\AutoLogin

````
install [Selenium](#Selenium).
````
pip install selenium

````

install [requests](#requests).
````
pip install requests

````

Now its time to setup drivers for chrome

Update chrome and Download Drivers from here : [chrome Driver](https://chromedriver.chromium.org/)
after downloading unzip file 
create this directory

````
C:\WebDriver\bin\

````
and place executable there.
#### for windows users
now use this command in CMD to add path 
````
setx /m path "%path%;C:\WebDriver\bin\"
````
now you all done

copy link of this repo or download it and place all the files into **AutoLogin** Directory and open CMD

do this
````
D:\python\prpject\Autologin > python auto.py

````
it will ask for your VUID and password after providing both of them hit enter and boom!!!! 
you are login and your **LMS is open**

## NEW FEATURES WILL BE ADD SOON

# ThANK YOU




