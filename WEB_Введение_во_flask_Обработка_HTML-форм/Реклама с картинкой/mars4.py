from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def mission():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def deviz():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion_image')
def image_mars():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" href="static/css/style.css">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                     <img src="static/img/mars.png" 
                     alt="здесь должна была быть картинка, но не нашлась">
                     <p class = 'green'>Человечество вырастает из детства.</p>
                     <p class = 'red'>Человечеству мала одна планета</p>
                     <p class = 'blue'>Мы сделаем обитаемыми безжизненные пока планеты.</p>
                     <p class = 'orange'>И начнем с Марса!</p>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
