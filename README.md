# bookService

Its a Book Service based on Flask


*Running Service*
flask run


*API*
 - GET
  http://127.0.0.1:5000/api/books  
    -Get all the books

- GET
  http://127.0.0.1:5000/api/books/<id>  
    -Get a bood with specific Id
 
 - POST
    - http://localhost:5000/api/books    
      - add a new book
      - { "author": "author5",   "id": 5,  "title": "titke5"    }

 
 - PUT
    - http://localhost:5000/api/books /4
      - update a new book
      - {  "author": "author55", "id": 5,  "title": "title55"    }



