from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
import os
import pyodbc

# Create an instance of the Flask class that is the WSGI application.
# The first argument is the name of the application module or package,
# typically __name__ when using a single module.

app = Flask("app", static_folder='static', template_folder="templates")

# Flask route decorators map / and /hello to the hello function.
# To add other resources, create functions that generate the page contents
# and add decorators to define the appropriate resource locators for them.

#connection_string="Driver={ODBC Driver 17 for SQL Server};Server=tcp:energyclerksqldb.database.windows.net,1433;Database=energyclerkSQLdb;Uid=sqladmin;Pwd=DBadmin123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
keyVaultName = os.environ["KEY_VAULT_NAME"]
sqluser_secretname=os.environ["USRNAME_SECRET"]
sqlpass_secretname=os.environ["SQLPASSWORD"]

KVUri = f"https://{keyVaultName}.vault.azure.net"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

print(f"Retrieving your secret from {keyVaultName}.")

retrieved_secret = client.get_secret(sqluser_secretname)

sqluser = '{retrieved_secret.value}'

retrieved_secret = client.get_secret(sqlpass_secretname)
sqlpassword = '{retrieved_secret.value}'

connection_string = str("Driver={ODBC Driver 17 for SQL Server};Server=tcp:"+os.environ['SQLSERVER_NAME']+",1433;Database="+os.environ['DBNAME']+";Uid="+{sqluser}+";")+"Pwd={"+{sqlpassword}+"};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"

field1=""
field2=""
print(connection_string)
with pyodbc.connect(connection_string) as conn:

    with conn.cursor() as cursor:
        cursor.execute("SELECT * from dbo.sample_table")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            field1=row[0]
            field2=row[1]
            row = cursor.fetchone()

@app.route('/')
def hello():
   # Render the page
   print("Request for Index page Received")
   return render_template('index.html', field1=field1, field2=field2)

if __name__ == '__main__':
   # Run the app server on localhost:4449
   app.run()

#end
