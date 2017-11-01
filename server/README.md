# Chatty Server
## Start
```
pip install -r requirements.txt
flask db upgrade  # Before do this, you must set FLASK_APP environment variable to run.py, and modify config.py
python run.py
```
## Test
```
pytest
```