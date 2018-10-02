# Jack Lu
# SoftDev1 pd8
# Kxx -- hwname
# 201x-xx-xx

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "index"

app.debug = True
app.run()
