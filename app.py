from flask import Flask,request,render_template
import requests

app=Flask(__name__)

@app.route('/index')
def homepage():
    return render_template('index1.html')

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5003)