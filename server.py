from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def render():
    return render_template('index.html')

host = "localhost"
port = "9000"

if __name__ == '__main__':
   app.run(host, port)