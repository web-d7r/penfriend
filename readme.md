App for searching penpals ([Demo](https://penfriendproject.herokuapp.com/)).  
It's a pycharm project, but you can run it on your computer, without pycharm. 
To do this, follow steps bellow:

* Clone repository(`git clone 'https://github.com/web-d7r/penfriend'`)
* Go inside it(`cd penfriend`)
* create virtual environment (`python3 -m venv venv`)
* install dependencies (`python3 -m pip install -r 'requirements.txt`' )
* make all migrations (`python3 manage.py makemigrations`)
* migrate (`python3 manage.py migrate`)
* create superuser(`python3 manage.py createsuperuser`)
* runserver (`python3 manage.py runserver`)  

Now, you can open app by this link `http://127.0.0.1:8000/` and register a new user.
You can also use admin panel from here `http://127.0.0.1:8000/admin`