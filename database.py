from config import *
from exceptions import *

import re
import os
import sqlite3
'''create_table_re = re.findall(r'CREATE TABLE \w+\((\w+ \w+(?:, )?)+\)')''' # for the future


class Database:
    def __init__(self, db_name):
        self.database = db_name
        self.connect = sqlite3.connect(self.database)

    def create_database(self, db_name, conn_return = False): # This function create new database and return connection to it
        try:
            dbcon = sqlite3.connect(str(db_name)+'.db') # Database connect
        except: # If name of db doesn't entered, the name of db = self.database
            db_name = str(self.database) + '.db'
            if conn_return == True:
                dbcon = sqlite3.connect(db_name)
                return dbcon



    def execute_query(self, dbname = None,
                      query = None): # This function executes the queries that will be entered
        connect = self.create_database(dbname)
        cur = connect.cursor()

        try:
            cur.execute(query)
            connect.commit() # Commit needs to save result of the query    
        
        except sqlite3.OperationalError:
            raise QueryError
    
    def execute_queries(self, dbname, queries): # This function execute some queries or saves them
        conn = self.create_database(dbname)
        cursor = conn.cursor()

        try:
            cursor.executescript(queries)
            conn.commit()

        except Exception as e:
            conn.rollback()
            raise e
        
        conn.close()


    def migration_function(self, dbname, queries): # This function needs to 'copy' database queries
        self.create_new_database(dbname) # tl - Table
        self.execute_queries(dbname, queries)


    def select_object(self, table_name, column_list = '*',
                      condition = ''): # This function select objects from table
        try:
            if len(condition) == 0:
                query_result = self.execute_query(f'SELECT {column_list} FROM {table_name}')
            else:
                query_result = self.execute_query(f'SELECT {column_list} FROM {table_name} WHERE {condition}')
            return query_result
        except sqlite3.OperationalError:
<<<<<<< HEAD
            raise TableNotFoundError

db = Database('test')
db.migration_function('test2','tl', 'tl2')
=======
            raise TableNotFoundError
>>>>>>> 4cd99247f4a64e5931ff0c9107ae050744c2f92d
