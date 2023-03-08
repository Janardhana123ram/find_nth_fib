# find_nth_fib
Return the nth fibonacci number

## Requirements
- Python3
- pip3 (sudo apt install python3-pip)
- Python3 virtualenv (sudo pip3 install virtualenv)
- git CLI

## Usage
### Setup
- Create python virtual environment (virtualenv -p python3 venv)
- Activate virtual environment (source vir/bin/activate)
- pip install -r requirements.txt

### Run migration commands
```
python manage.py makemigrations
python manage.py migrate
```

### Start server
```
python manage.py runserver
```

<b>Use below API to return nth fibonacci number</b>
```
POST http://127.0.0.1:8000/fibonacci
request-body: {'n': 10}
```

<b>Use below API to return all stored nth fibonacci numbers in the DB</b>
```
GET http://127.0.0.1:8000/fibonaccis
```
