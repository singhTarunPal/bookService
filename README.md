# bookService

*Description:* Its a Book Service to manage the book records

*Author:* Tarun Pal Singh

*Design:* ITs a Microservice based on Flask and SQLite 


## Setting up env
 - Installing Vitual ENV
 	- pip install virtualenv
 - Create virtualenv for windows
 	- py -3 -m venv venv
 - Activate virualenv for windows
 	- venv\Scripts\activate
 - Install Flask on the enviroment
 	- pip install flask
 - Upgrading PIP
 	- python -m pip install --upgrade pip

## Running Service
 - flask run


## API
 - GET
  http://127.0.0.1:5000/api/books  
    -Get all the books
    -	Sample Response: [ {"author": "Author1","created": "2022-04-03 15:10:41","id": 1, "title": "Title1"},
			{"author": "Author2","created": "2022-04-03 15:11:41","id": 2, "title": "Title2"}]

- GET
  http://127.0.0.1:5000/api/books/<id>  
    -Get a book with specific Id
    -	Sample Response: [ {"author": "Author2","created": "2022-04-03 15:11:41","id": 2, "title": "Title2"}]

 
 - POST
    - http://localhost:5000/api/books    
      - add a new book
      - { "author": "author5",   "id": 5,  "title": "title5"    }

 
 - PUT
    - http://localhost:5000/api/books/4
      - update a new book
      - {  "author": "author55", "id": 5,  "title": "title55"    }


## Reference
 - https://www.digitalocean.com/community/tutorials/how-to-use-an-sqlite-database-in-a-flask-application
 - https://dzone.com/articles/python-flask-code-generator
 - https://flask.palletsprojects.com/en/2.0.x/quickstart/
