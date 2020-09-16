# How to start development

## MacOS
```
python -m venv myenv
source myenv/bin/activate
pip install flask
```

### start server
```
export FLASK_ENV=development
flask run --host=0.0.0.0
```

then, please go to
http://localhost:5000/hello

## import/export your environment
### import
```
pip install -r requirements.txt
```

### export
```
pip freeze > requirements.txt
```

## migrate db
```
$ python3
>>> from models.database import init_db
>>> init_db()
```