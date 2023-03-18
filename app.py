from flask import Flask, render_template
import random

app = Flask(__name__)

lower = "qwertyuiopasdfghjklzxcvbnm"
upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
numbers = "0123456789"
symbols = "[]{}()*;/,._-"

all = lower + upper + numbers + symbols
length = 16
password = "".join(random.sample(all,length))

@app.route('/')
def index():
    return render_template('home.html', password="".join(random.sample(all,length)))

if __name__ == '__main__':
    app.run(debug=True, port='8080')