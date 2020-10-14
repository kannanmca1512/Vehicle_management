# Vehicle_management
Designed to implemented for storing vehicle details and implementation of social login


#steps to follow
1. ./rebuiddb 
      Django basic configurations commands where associated within this file. It will executes the following commands:-
      rm -rf db.sqlite3
      python manage.py makemigrations 
      python manage.py migrate 
      python manage.py init
      
      where python manage.py init creates a default user whose username is "admin" and password is "superadmin@123"
2. python manage.py runserver
3. Social login where implemented, both login with facebook and login with google
      In order to work these login functionalities add the corresponding clientId , secret keys to the social application from django admin.
