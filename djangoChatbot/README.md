# Chatbot based on Django
## Team Members: Ishan Adhaulia, Anurag Nigam & Davy Baardink

## Dataset
The dataset has been obtained from open source project namely **[Link](https://github.com/gunthercox/chatterbot-corpus)**

 ## Requirements

- Python 3
- Django > 2.1.4

## Summary 
```
Steps for creating project
1. Create project
2. Create an app within the project
3. Write a view (myapp/views.py)
4. Design URLs within the app (myapp/urls.py)
5. Join app URL conf (urls.py)
6. Register app myapp/apps.py (myproject/settings.py)
7. Test python manage.py runserver

Steps for linking db with project
1. Setup database (myproject/settings.py)
2. Create models (myapp/models.py)
3. Register admin (myapp/admin.py)
4. Run makemigrations, migrate,createsuperuser
```
## Project Structure
This project follows the standard folder structure like any other django-based project. 
```
Chatbot_TT/         -> directory for project

  db.sqlite3        -> db choice
  manage.py         -> runner for server, creating superuser, etc
  Chatbot_TT/      
    __init__.py	
    settings.py	    -> project settings
    urls.py	        -> project's listed urls 
    wsgi.py         -> WSGI config for project.
  
  chatapp/          -> application (in our case, its chatbot)
    migrations/     
    static/       
      js/
        bot.js      -> JS file for handling UX 
    templates/
      chatapp/
        bot.html    -> Bot Homepage for UI
        index.html  -> Index page for chatbot
    __init__.py
    admin.py        -> registering the chatapp with admin
    apps.py         -> Application config definition
    models.py       -> Django Model for handling requests
    tests.py        -> Unit test cases
    urls.py         -> Application's listed urls 
    views.py        -> User defined Views for the application
```

## Important classes or definition

Table defined in the db as 
```
CREATE TABLE "chatapp_chatinfo" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"question" varchar(200) NOT NULL, "answer" varchar(2000) NOT NULL,
"category" varchar(100) NOT NULL)
```

Model defined in the project
```
class ChatInfo(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=2000)
    category = models.CharField(max_length=100)

    # Returns answer for the particular model object
    def __str__(self):
        return self.answer
```

Python code for accessing data from db. The above defined str function directly outputs the required field.
```
response = str(ChatInfo.objects.get(question=userinput))
```
