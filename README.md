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

# import/export your environment
## import
```
pip install -r requirements.txt
```

## export
```
pip freeze > requirements.txt
```

# migrate db
## init
```
$ python3 migrate_db.py
```
## insert data
```python
>>> from models.database import db_session
>>> from models.models import Videos
>>> v1 = Videos('5MIN BOOTY & AB WORKOUT // Yoga Ball | Pamela RF', '2020/9/15', 'The video is in full length which means you can just follow whatever I’m doing! 30 seconds each exercise – NO REST IN BETWEEN.','','https://youtu.be/iY4hQd24_d0','exercise')
>>> db_session.add(v1)
>>> db_session.commit()
```

## check db
```shell
$ cd models
$ sqlite3 healthcare.db
sqlite> select * from videos;
```