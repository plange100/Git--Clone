import mysql.connector
import hashlib
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()
# print(os.getenv("password"))

config = {
  'host' : os.getenv('host'),
  'user' : os.getenv('user'),
  'password' : os.getenv('password'),
  'database' : os.getenv('database')
}
# print(config)

def check(db):
  cursor = db.cursor()
  cursor.execute("SHOW TABLES")
  tables = cursor.fetchall()

  for t in tables:
    print(t[0])
    if(t[0] == "login"):
      print("login table found!")

db = mysql.connector.connect(**config)
check(db)
db.close()


def adduser():
  db = mysql.connector.connect(**config)
  user = input("Enter user id: ")
  pwd = input("Enter password: ")
  hashpw = hashlib.sha256(pwd.encode("utf-8")).hexdigest()
  db.commit()
  if(cursor.rowcount == 1):
    print("Success")
  else:
    print("Try again")
  db.close()
  return

def login():
  db = mysql.connector.connect(**config)
  userid = input("Enter userid: ")
  pwd = input("Enter password: ")
  hashpw = hashlib.sha256(pwd.encode("utf-8")).hexdigest()
  cursor = db.cursor()
  sql = "SELECT * FROM login WHERE user = %s and password =%s"
  user = (userid, hashpw)
  cursor.execute(sql, user)
  result = cursor.fetchall()
  db.close()

  if(len(result)==1):
    print("Success")
    return True
  else:
    print('Fail')
    return False
  

def check_login():
  if login():
    print("User is logged in")
  else:
    print("User is not logged in")

while True:
  print("*** Python and MySQL Login System")
  loggedin = False
  i = input(" 1 to register \n 2 to login \n 3 to check login \n Any other key to exit")
  if i == '1':
    adduser()
  elif i == '2':
    login() #test login
  elif i == '3':
    check_login() #test if logged in
  else:
    print("Exiting...!")
    break


adduser()