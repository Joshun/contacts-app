# contacts-app

To setup:
1. Install Python3.11 (or higher)
2. Create a virtual environment and install the required dependencies
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Run the Django migrations
```
python manage.py migrate
```

4. Create a user account
```
python manage.py createsuperuser
```

You can then use this account to login

5. Run the project
6. ```
   python manage.py runserver
   ```

   Should by default open in http://localhost:8000 (but if it chooses another URL it will tell you).
   You can login with the superuser you have created. If you want to create additional user accounts, you can do this after logging in by going to the admin page (/admin url)


   To run unit tests:
   ```
   python manage.py test
   ```

   
