# Play Game App
It is an app build with django to play game in which a user selects resembling secondary image with a primary image. User gets 5 questions and he competes with another user and gets score when another user with whom he is competing also selects the same answers.
This application comes with
  - html5
  - jQuery
  - Twitter Bootstrap
  
and also requirements.text file is
```sh
appdirs==1.4.0
Django==1.10.5
packaging==16.8
pyparsing==2.1.10
six==1.10.0
```
### Features!

  - Pairing of Players.
  - LogIn, LogOut and SignUp
  - Can see Scorecard
  - Play as many games as you want
### Installation
#### 1. Virtualenv

You should already know what is virtualenv. So, simply create it for your own project, where projectname is the name of your project:
```sh
$ virtualenv projectname
```

##### 2.Download

Now, you need this Game project files in your workspace,So you can clone it easily
```sh
git clone git@github.com:viru1404/PlayGame.git
```

##### 3.Requirements

You can find all requirements in requirements.txt file and easily install them with
```sh
$ pip install -r requirements.txt
```

##### 4.Initialize the database

First set the database engine (PostgreSQL, MySQL, etc..) in your settings files; Of course, remember to install necessary database driver for your engine. Then define your credentials as well.:
```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

Now Run the local server using command below and check localhost(http://127.0.0.1:8000/ ).
```sh
$ python manage.py runserver
```
