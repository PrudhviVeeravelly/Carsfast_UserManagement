# Carsfast_UserManagement

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

    Python >= 3.6
    Django >= 4.2.4
    

### Installation

1. Clone the repository

```
git clone https://github.com/YourUsername/Carsfast_UserManagement.git
cd Carsfast_UserManagement
```

2. Configure the database settings in settings.py.

3. Apply database migrations:

```
python manage.py migrate

4. Create a superuser account for initial access:

   ```
   python manage.py createsuperuser

5. Run the development server

   ```
   python manage.py runserver
   ```
### Testing

    1. Access the admin panel by navigating to http://localhost:8000/admin/ and log in with the superuser account you created.

    2. Use the admin panel to manage users and their data.

    3. Test Basic Authentication:

       
       curl -X POST -d "username=<username>&password=<password>" http://127.0.0.1:8000/api/login/


    4. Access the protected resources

      
      curl -H "Authorization: Bearer <your_access_token>" http://127.0.0.1:8000/api/protected/

    5. Test downloaded and delete the user data

       
       curl -H "Authorization: Bearer <your_access_token>" http://127.0.0.1:8000/api/download_user_data/
       curl -X POST -H "Authorization: Bearer <your_access_token>" http://127.0.0.1:8000/api/delete_user_data/





