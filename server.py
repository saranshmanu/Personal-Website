from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def render():
    return render_template('index.html')

@app.route('/achievements')
def renderAchievements():
    return render_template('achievements.html')

@app.route('/robots.txt')
def siteMap():
    return app.send_static_file('robots.txt')

@app.route('/sitemap.xml')
def robotsTxt():
    return app.send_static_file('sitemap.xml')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

host = "0.0.0.0"
port = "80"

if __name__ == '__main__':
   app.run(host, port)
