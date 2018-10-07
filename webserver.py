from flask import Flask, send_from_directory
app = Flask(__name__,static_url_path='')

@app.route('/')
def serve_home():
    return send_from_directory('webassets', 'index.html')


@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('webassets/static', path)


@app.route('/rss')
def serve_rss_file():
    return send_from_directory('.', 'discord.xml')


app.run(debug=True)