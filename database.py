"""
*   version 1.0
*   author : david
*   desc : database manager 
*   contain function which stock rules into database sqlite
*   and for the corresponding code
"""
import sqlite3
import os

class database:
    """class for manage the rules into the database"""
    def __init__(self, db_name):
        """database constructor, it find the directory name and create or open
        the database of the project"""
        self.db_name = db_name
        self.path = os.getcwd()
        self.db = sqlite3.connect(self.path + os.sep + 'database' + os.sep +  self.db_name)	
        self.cursor = self.db.cursor()
        
    def __del__(self):
        """close the cursor when the class is deleted"""
        self.db.close()
        
    def create_tables(self):
        """create the table for the rules and code
        table schema label | code"""
        try:
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
            (LOGIN TEXT PRIMARY KEY, PW TEXT)''')
	    self.cursor.execute('''CREATE TABLE IF NOT EXISTS credentials
	    (ID TEXT, PW TEXT, APP TEXT, LOGIN TEXT, FOREIGN KEY(LOGIN) REFERENCES users(LOGIN))''')
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
               
        
    def insert_user(self, login, pw):
        """insert a new rules into the database"""
        try:
            self.cursor.execute('''INSERT OR REPLACE INTO users VALUES (?, ?)''', [login, pw])
	    self.db.commit()
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])

    def insert_creds(self, ident, pw, login):
        """insert a new rules into the database"""
        try:
            self.cursor.execute('''INSERT OR REPLACE INTO credentials VALUES (?, ?, ?)''', [ident, pw, login])
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
            
    def select_users(self):
        """select all the rules into the database"""
        try:
            return self.cursor.execute('''SELECT * FROM users''')
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
        
    def select_by_login(self, login):
        """select the code associated to the label in entry"""
        try:
            return self.cursor.execute('''SELECT * FROM users WHERE login = (?)''', [login])
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
        
    def select_creds(self, login):
        """select the label associated to the code in entry"""
        try:
            return self.cursor.execute('''SELECT * FROM credentials WHERE login = (?)''', [login])
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
            
    def delete_user(self, login):
        """delete the only rules associated to the label and the code"""
        try:
            self.cursor.execute('''DELETE FROM users WHERE login = (?)''', [login])
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])     
    
    def delete_creds(self, login):
        """delete all the rules associated to this label""" 
        try:
            self.cursor.execute('''DELETE FROM users WHERE login = (?)''', [login])
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])    
        
    def delete_by_code(self, code):
        """delete all the rules associated to this code"""
        try:
            self.cursor.execute('''DELETE FROM users WHERE code = (?)''', [code])
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
