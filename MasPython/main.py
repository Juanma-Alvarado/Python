# -*- coding: utf-8 -*-

from flask import Flask, reder_template

app = Flask(__name__)

@app.route('/')
def hola():
    return reder_template('hola')

if __name__ == '__main__':
    app.run()