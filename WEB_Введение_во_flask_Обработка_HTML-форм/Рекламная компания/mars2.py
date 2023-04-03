from flask import Flask

app = Flask(__name__)


@app.route('/')
def mission():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def deviz():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def  reklama():
    with open('reklama.html', 'r', encoding='utf-8') as html_stream:
        return html_stream.read()


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
