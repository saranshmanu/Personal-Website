from flask import Flask, redirect, url_for, request, render_template, after_this_request
from flask_compress import Compress
from io import StringIO as IO, BytesIO
import gzip
import functools

def gzipped(f):
    @functools.wraps(f)
    def view_func(*args, **kwargs):
        @after_this_request
        def zipper(response):
            accept_encoding = request.headers.get('Accept-Encoding', '')
            if 'gzip' not in accept_encoding.lower():
                return response
            response.direct_passthrough = False
            if (response.status_code < 200 or
                response.status_code >= 300 or
                'Content-Encoding' in response.headers):
                return response
            gzip_buffer = BytesIO()
            gzip_file = gzip.GzipFile(fileobj=gzip_buffer, mode='w')
            gzip_file.write(response.data)
            gzip_file.close()
            response.data = gzip_buffer.getvalue()
            response.headers['Content-Encoding'] = 'gzip'
            response.headers['Vary'] = 'Accept-Encoding'
            response.headers['Content-Length'] = len(response.data)
            return response
        return f(*args, **kwargs)
    return view_func

app = Flask(__name__)
Compress(app)

@app.route('/')
@gzipped
def render():
    return render_template('index.html')

@app.route('/journey')
@gzipped
def resume():
    return render_template('journey.html')

@app.route('/achievements')
@gzipped
def renderAchievements():
    return render_template('achievements.html')

@app.route('/robots.txt')
@gzipped
def siteMap():
    return app.send_static_file('robots.txt')

@app.route('/sitemap.xml')
@gzipped
def robotsTxt():
    return app.send_static_file('sitemap.xml')

@app.errorhandler(404)
@gzipped
def page_not_found(e):
    return render_template('error.html'), 404

host = "0.0.0.0"
port = "80"

if __name__ == '__main__':
   app.run(host, port, debug=True)

