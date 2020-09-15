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