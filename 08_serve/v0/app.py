'''
Team Brown: Nakib Abedin, Eric Sohel, Shafiul Haque
SoftDev pd08
K07 - TEARDOWN
2022-09-22
time spent: 0.5hrs
'''

from flask import Flask
app = Flask(__name__) # ...

@app.route("/") # ...
def hello_world():
    print(__name__) # ...
    return "No hablo queso!"  # ...

app.run()  # ...