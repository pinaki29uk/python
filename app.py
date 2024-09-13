from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)
import os

# Create an instance of the Flask class that is the WSGI application.
# The first argument is the name of the application module or package,
# typically __name__ when using a single module.

app = Flask("app", static_folder='static', template_folder="templates")

# Flask route decorators map / and /hello to the hello function.
# To add other resources, create functions that generate the page contents
# and add decorators to define the appropriate resource locators for them.

@app.route('/')
def hello():
   # Render the page
   print("Request for Index page Received")
   return render_template('index.html')

if __name__ == '__main__':
   # Run the app server on localhost:4449
   app.run()

#end
