import requests
import random
import string
from flask import Flask,render_template,request
app=Flask(__name__)

def funcPassword(length):
    char = string.ascii_letters + string.digits + string.punctuation
    result = ''.join(random.choice(char) for _ in range(length))
    return result

@app.route('/')
def index():
    return render_template('input.html')

@app.route('/', methods=['POST'])
def process_input():
    n = request.form['user_input']
    if n=='':
        passwd="ERROR: Empty password"
    elif (n.isdigit() and int(n)>100):
        passwd="ERROR: password length must be less than 100"
    elif(n.isdigit() and int(n)>0):
        passwd=funcPassword(int(n))
    elif(n[0]=='+' and n[1:].isdigit() and int(n)>0 and int(n)<100):
        passwd=funcPassword(int(n))
    elif (n[0]=='-' and n[1:].isdigit() and int(n)<=0):
        passwd="ERROR: enter a valid LENGTH value"
    elif (n.isdigit() and int(n)==0):
        passwd="ERROR: password length must be greater than zero"
    elif ((n[0]=='-' or n[0]=='+') and n[:1].isdigit() and int(n)==0):
        passwd="ERROR: password length must be greater than zero"
    else:
        passwd="ERROR: INVALID PASSWORD"
    return render_template('password.html',Result=passwd)

if __name__=="__main__":
    app.run(debug=True)
