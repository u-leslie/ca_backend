# 1. Clone & cd
git clone  https://github.com/u-leslie/ca_backend.git <br/>
cd ca_backend

# 2. Create virtualenv
python -m venv .venv <br/>
source .venv/bin/activate

# 3. Install deps
pip install -r requirements.txt

# 4. Migrate
python manage.py makemigrations <br/>
python manage.py migrate

# 5. Create superuser (admin for all apps)
python manage.py createsuperuser

# 6. Run
python manage.py runserver
