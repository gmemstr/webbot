from flask import Flask, send_from_directory
import config


def main():
    app = Flask(__name__, static_url_path='')

    @app.route('/')
    def serve_home():
        return send_from_directory('webassets', 'index.html')

    @app.route('/static/<path:path>')
    def send_js(path):
        return send_from_directory('webassets/static', path)

    @app.route('/rss')
    def serve_rss_file():
        return send_from_directory('.', 'discord.xml'), 200, {'Content-Type': 'application/rss+xml'}

    Flask.run(app, port=config.flaskport, debug=config.flaskdebug)


if __name__ == '__main__':
    main()
