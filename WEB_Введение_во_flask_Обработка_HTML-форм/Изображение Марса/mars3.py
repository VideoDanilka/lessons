from flask import Flask

app = Flask(__name__)


@app.route('/')
def mission():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def deviz():
    return 'И на Марсе будут яблони цвести!'


@app.route('/image_mars')
def image_mars():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                     <img src="static/img/mars.png" 
                     alt="здесь должна была быть картинка, но не нашлась">
                     <p>Вот она какая, красная планета.<p>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
