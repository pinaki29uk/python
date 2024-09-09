from flask import Flask
import os
import pyodbc
import uvicorn

# Create an instance of the Flask class that is the WSGI application.
# The first argument is the name of the application module or package,
# typically __name__ when using a single module.
app = Flask(__name__)

# Flask route decorators map / and /hello to the hello function.
# To add other resources, create functions that generate the page contents
# and add decorators to define the appropriate resource locators for them.

@app.route('/')
@app.route('/hello')
def hello():
   # Render the page
   return "Hello Python!"

if __name__ == '__main__':
   # Run the app server on localhost:4449
   #app.run(debug=True, host='0.0.0.0')
   uvicorn.run()

##connection_string = str("Driver={ODBC Driver 17 for SQL Server};Server=tcp:energyclerksqldb.database.windows.net,1433;Database=energyclerkSQLdb;Uid=sqladmin;Pwd=DBadmin123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")


connection_string = str("Driver={ODBC Driver 17 for SQL Server};Server=tcp:"+os.environ['SQLSERVER_NAME']+",1433;Database="+os.environ['DBNAME']+";Uid="+os.environ['USRNAME']+";")+"Pwd={"+os.environ['PASSWORD']+"};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"

print("connection string")
print(connection_string)
with pyodbc.connect(connection_string) as conn:

    with conn.cursor() as cursor:
        cursor.execute("SELECT * from dbo.sample_table")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()
