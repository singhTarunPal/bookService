# bookService

Its a Book Service based on Flask

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
      - { "author": "author5",        "created": "2022-03-28 15:08:39",        "id": 5,        "title": "titke5"    }

 
 - PUT
    - http://localhost:5000/api/books /4
      - update a new book
      - {  "author": "author55", "created": "2022-03-28 15:08:39", "id": 5,  "title": "title55"    }



