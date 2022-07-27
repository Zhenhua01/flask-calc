# Put your app in here.

from flask import Flask, request
import operations

app = Flask(__name__)

@app.get('/add')
def add_nums():

    a = int(request.args["a"])
    b = int(request.args["b"])

    return str(operations.add(a, b))