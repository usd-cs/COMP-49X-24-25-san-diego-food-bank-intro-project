# COMP-49X-24-25-san-diego-food-bank-intro-project

Overview:
    Our message posting application is a Django powered web forum that is designed 
    to display various user engagements through posts and comments. Users can sign in to their 
    account and participate in discussions by making posts or commenting on others' posts.
    Our application has an intuitive and easy to use user interface for effortless navigating 
    and interaction.

Features:
    - User Authentication: Users can log in and log out securely. The application also can 
    distinguish between regular users and admins, allowing admins special permissions. 

    -Post Creation: Users who are logged in can create new posts in a timeline format. Each post 
    is associated with whatever user created it and also includes a timestamp for when it was created. 

    -Commenting: Users can comment on posts, allowing them to be involved in discussions and interact with other users. 

    -Admin: Admin users can manage posts and comments, giving them control over content or user interactions. 

Installation:

1. Clone the repo: 
    https://github.com/usd-cs/COMP-49X-24-25-san-diego-food-bank-intro-project.git  
    or 
    git@github.com:usd-cs/COMP-49X-24-25-san-diego-food-bank-intro-project.git 

2. Install required dependencies (pip install):
    pytest==8.3.3
    django==5.1.3
    sqlparse==0.5.1
    asgiref==3.8.1
    psycopg2==2.9.10 

3. Setup the PostgreSQL database:
    python manage.py migrate 

4. Create a superuser account to access the admin:
    python manage.py createsuperuser 

5. Run the development server and visit http://127.0.0.1:8000 to access via browser:
    python manage.py runserver 