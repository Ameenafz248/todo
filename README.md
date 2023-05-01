### TaskMate
##### A simple Django todo app to create, check and delete tasks
## Features
- Full authentication support using django-allauth
- Dynamically create, update and delete task which are already done
- Separate sections for unfinished and finished tasks
- Search bar to filter the tasks
- Responsive design : smartphone-friendly

## Built With
- Django for backend 
- HTML, CSS and vanilla JS for the frontend

## Getting Started
1. Clone the repository
    ```
    git clone https://github.com/Ameenafz248/todo.git
    cd todo
    ```
2. Create and  activate virtual environment
    ```
    python3 -m venv .venv
    source .venv/bin/activate
    ```
3. Install the dependencies
    ```
    python3 -m pip install -r requirements.txt
    ```
4. Get a secret key
    ```
    python3 -c "import secrets; print(secrets.token_urlsafe())"
    ```
5. Setup environmental variables
    ```
    vim .env
    ```
6. Put this code inside .env:

    ```
    DEBUG=True
    SECRET_KEY=abcdefghijklmopqrstuvwxyz //the secret_key you created using secrets library
    DJANGO_SECURE_SSL_REDIRECT=False
    DJANGO_SECURE_HSTS_SECONDS=2592000
    DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS=False
    DJANGO_SECURE_HSTS_PRELOAD=False
    DJANGO_SESSION_COOKIE_SECURE=False
    DJANGO_CSRF_COOKIE_SECURE=False
    ```

7. Make migrations
    ```
    python3 manage.py migrate
    ```
8. Run the program
    ```
    python3 manage.py runserver
    ```