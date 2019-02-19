from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def render():
    return render_template('index.html')

@app.route('/achievements')
def renderAchievements():
    return render_template('achievements.html')

host = "0.0.0.0"
port = "80"

if __name__ == '__main__':
   app.run(host, port)
