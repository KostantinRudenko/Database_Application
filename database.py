from config import *
from exceptions import *
from engine import *

import re
import os
import sqlite3
import datetime


class Database:
    def __init__(self, db_name):
        self.database = db_name
        self.connect = sqlite3.connect(self.database+'.db')

    def create_database(self, db_name):
        # This function create new database and return connection to it
        try:
            dbcon = sqlite3.connect(str(db_name)+'.db') # Database connect
            return dbcon
        except: # If name of db doesn't entered, the name of db = self.database
            db_name = str(self.database) + '.db'
            dbcon = sqlite3.connect(db_name)
            return dbcon

    def execute_query(self, query = None): 
        cur = self.connect.cursor()

        try:
            cur.execute(query)
            self.connect.commit() # Commit needs to save result of the query    
        
        except sqlite3.OperationalError:
            raise QueryError
    
    def execute_queries(self, queries, 
                        is_select = False, close_status = False):
        # This function execute some queries or saves them
        cursor = self.connect.cursor()
        result_string = '' # result_string - final string with result of the query
        all_select_queries = ''
        if is_select:
            select_queries = re.findall(SELECT_QUERY, queries)
            for select_query in select_queries:
                all_select_queries += select_query+'\n'
                queries = queries.replace(select_query, '')

            for select_query in select_queries: 
                current_date = datetime.datetime.today()
                current_date = current_date.strftime(TIME_FORMAT)    
                results = cursor.execute(select_query).fetchall()
                result_string += f'------RESULT FOR THE {current_date}------\n'
                for result_tuple in results:
                    for result_str in result_tuple:
                        result_string += str(result_str)+'\n'      
        else:
            cursor.executescript(queries)
            self.connect.commit()
            if close_status:
                self.connect.close()
        return result_string


    def migration_function(self, dbname, queries): # This function needs to 'copy' database queries
        self.create_database(dbname)
        self.execute_queries(queries)