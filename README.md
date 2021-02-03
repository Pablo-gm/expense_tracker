# Zenexpender
A simple expense tracker project to manage personal finance.

## Install
Once you have python installed on your computer.

Clone project
```c
git clone https://github.com/Pablo-gm/expense_tracker.git
```

Create a virtualenv inside project folder with any name you want for example:
```c
python -m venv myvenv
# or
virtualenv myvenv
```

Activate virtualvenv `myvenv`
```c
# Windows
myvenv\Scripts\activate.bat 

# Gitbash
cd myvenv\Scripts\
. activate

# Linux
source virtualenv myvenv/bin/active
```

Install requirements
```
pip install -r requirements.txt
```

Run migrations
```
python manage.py migrate
```

Optional: create superuser
```
python manage.py createsuperuser

# Gitbash
winpty python manage.py createsuperuser
```

Run server
```
python manage.py runserver
```

Check project on http://127.0.0.1:8000/

## Notes

### CSS
Project use Bootstrap v 5.0.0 and SASS, to compile a css file run:
```
sass static/sass/main.scss static/css/main.css
```

Another way is to add css directly on static\css\custom.css and remove the comment from templates\general\header
```
<!-- <link rel="stylesheet" href="{% static '/css/custom.css' %}"> -->
```
