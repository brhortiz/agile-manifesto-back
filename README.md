# agile-manifesto-back
The backend counterpart of agile-manifesto. It contains all the API endpoints used in the exercise.

Requires Python v3.8.5 and Pip

## Setup
Assuming you have cloned this repository and met the requirements, it is recommended to use a virtual environment

```
pip install virtualenv
```
Create a virtual environment
```
virtualenv env
```
Activate it 
```
source env/bin/activate
```
You'll see an `(env)` in the terminal if it works.

Install the dependencies
```
pip install -r requirements.txt
```

Migrate models to the database, it will automatically add an sqlite.
```
python manage.py migrate
```

Run the server
```
python manage.py runserver 8000
```

Done!