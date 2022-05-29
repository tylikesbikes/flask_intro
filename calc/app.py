# Put your app in here.
from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route('/add')
def route_add():
    return str(add(int(request.args['a']),int(request.args['b'])))

@app.route('/sub')
def route_sub():
    arg_a = int(request.args.get('a'))
    arg_b = int(request.args.get('b'))
    return str(sub(arg_a,arg_b))

@app.route('/mult')
def route_mult():
    arg_a = int(request.args.get('a'))
    arg_b = int(request.args.get('b'))
    return str(mult(arg_a,arg_b))

@app.route('/div')
def route_div():
    arg_a = int(request.args.get('a'))
    arg_b = int(request.args.get('b'))
    return str(div(arg_a,arg_b))

@app.route('/math/<operation>')
def do_math(operation):
    ops = {
        'add':route_add,
        'sub':route_sub,
        'mult':route_mult,
        'div':route_div
    }

    return ops[operation]()