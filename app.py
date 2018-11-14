# Jack Lu
# SoftDev1 pd8
# Kxx -- hwname
# 201x-xx-xx

# stdlib
import json
from urllib import request

# pip install
from flask import Flask, render_template

# custom modules
app = Flask(__name__)

@app.route('/')
def index():
    return "index"

KEY = ""
URL_STUB = ""
URL = URL_STUB + KEY

app.debug = True
app.run()
