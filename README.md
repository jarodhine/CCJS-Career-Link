# CCJS-Career-Link
CP3405 Career Link App


Windows Enviroment Setup:
//Run command prompt as administrator
//$ denotes a command to be entered into a command prompt
  
  Install Git
  Install python 3.6 or greater
  Download get-pip.py
  $python get-pip.py
  $python -m pip install --upgrade pip
  $pip install virtualenv

Project Setup
  (Choosen Directory)$git clone https://github.com/jarodhine/CCJS-Career-Link
  $virtualenv --no-site-packages
  $source env/bin/activate
  $pip install -r requirements.txt
  $python ./manage.py syncdb
  $python ./manage.py migrate
  $python ./manage.py runserver
