python -m venv env
env\Scripts\activate.bat
pip install -r requirements.txt
python manage.py test
start "" http://localhost:8000
python manage.py runserver 8000