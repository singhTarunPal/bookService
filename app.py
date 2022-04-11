

from operator import eq
import sqlite3
from flask import Flask
from flask import jsonify
from flask import request
from flask import json

app = Flask(__name__)

def get_db_conn():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def hello():
	return "welcome to the flask app for books-By Tarun"
	
	
@app.route('/api/books',methods=['GET'])
def getAllBooks():    
    con = get_db_conn()
    cur = con.cursor()
    cur.execute('''SELECT * FROM books''')
    row_headers=[x[0] for x in cur.description] #this will extract row headers
    rv = cur.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return jsonify(json_data)    
    

@app.route('/api/books/<bookId>',methods=['GET'])
def getEmp(bookId):
    con = get_db_conn()
    cur = con.cursor()
    cur.execute("SELECT * FROM books WHERE id = '%s'" % bookId)
    row_headers=[x[0] for x in cur.description] #this will extract row headers
    rv = cur.fetchall()
    con.close
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return jsonify(json_data)  

@app.route('/api/books',methods=['POST'])
def createBook():
    
    a=request.json['id']
    b=request.json['author']
    c=request.json['title']
    con = get_db_conn()
    cur = con.cursor()
    cur.execute("insert into books (id, author, title)  values (?, ?, ?)", (a, b, c))
    con.commit()
    con.close
    return jsonify({'response':'Success', 'id' : a, 'title' : c, 'author': b })


@app.route('/api/books/<bookId>',methods=['PUT'])
def updateBook(bookId):
    a=request.json['id']
    b=request.json['author']
    c=request.json['title']

    con = get_db_conn()
    cur = con.cursor()
    rows = cur.execute("SELECT * FROM books WHERE id = '%s'" % bookId).fetchall()
    print (len(rows))
    if len(rows) > 1 :
        return jsonify({'response':'More than 1 records found'})
    else : 
        if len(rows) > 0:
            cur.execute("update books set author = ? , title = ? where id = '%s'"  %a, (b,c))
            con.commit()
            con.close
            return jsonify({'response':'Success', 'id' : a,  'author': b, 'title' : c})    
        else:
            return jsonify({'response':'No record found'}) 

    
@app.route('/api/books/<bookId>',methods=['DELETE'])
def deleteEmp(bookId):
    con = get_db_conn()
    cur = con.cursor()
    rows = cur.execute("SELECT * FROM books WHERE id = '%s'" % bookId).fetchall()
    print (len(rows))
    if len(rows) > 0 :
        cur.execute("DELETE FROM books WHERE id = '%s'" % bookId)
    else :
        return jsonify({'response':'No record found'})   
    con.commit()
    con.close
    return jsonify({'response':'Success'})

if __name__ == "__main__":
	app.run(host ='0.0.0.0', port = 5000, debug = True)