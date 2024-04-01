Key Takeaways
[Data Management in Python Login System]

Task 1
Create a MySQL database table to store logins:

We can use the MySQL shell to create a database table.

The database is created first, using the create database command:  create database users;

To select the database, we use the command use: use users;

The table is created using the create table command with appropriate data types in the fields: create table login ( user varchar(255), password varchar (255));

Add a primary key to prevent duplicate entries: alter table users add primary key(user);

Task 2
Connect to the MySQL login database using Python: 

To access the MySQL connector, we import package mysql.connector:

A .env file can be created to contain connection config parameters such as MySQL Server, a userid, password, and    database name:

              database=users

              password=adminadmin

              user=root

              host=localhost

The environment is loaded using the load_dotenv function and the os object gets the env variables for the MySQL connection.


Task 3
Check for the existence of the database using Python:

The connect object has a cursor object that contains functions to interface with the MySQL database: cursor = db.cursor()

The execute command is used to issue instructions to the MySQL database: cursor.execute("SHOW TABLES")

The cursor can then fetch results, for example, into a list: tables = cursor.fetchall()

Task 4
Use Python to Insert a userid and password into the login database: 

The password should be encrypted before insertion into a database: hashpw = hashlib.sha256(pwd.encode("utf-8")).hexdigest() 

To form the insert SQL, we use a string with escape characters to form the data values: sql = "INSERT INTO login (user, password) VALUES (%s, %s)"

When we form the values, we use a tuple format: values = (user, hashpw)

With a single value, a comma is required for tuple format: values = (user,) would be used.

The insert command is issued with the SQL and values using the cursor’s execute function: cursor.execute(sql, values)

Task 5
Query the database to check for a userid and password using Python:

Once the user and password are obtained, the password is encrypted to check it against the encrypted password in the database: hashpw = hashlib.sha256(pwd.encode("utf-8")).hexdigest()

The Select.. Where query is used to check for their existence in the database: sql = "SELECT * FROM login WHERE user = %s and password = %s"

The cursor then contains the number of entries in the result, which should be one in the case of a unique user and password: if (cursor.rowcount == 1): …

____________________

Additional Resources: 

https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html 

https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html 