from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def mission():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def deviz():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    with open('promotion.html', 'r', encoding='utf-8') as html_stream:
        return html_stream.read()


@app.route('/promotion_image')
def image_mars():
    with open('promotion_image.html', 'r', encoding='utf-8') as html_stream:
        return html_stream.read()


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        with open('astronaut_selection.html', 'r', encoding='utf-8') as html_stream:
            return html_stream.read()
    elif request.method == 'POST':
        print(request.form['class'])
        print(request.form['sex'])
        return "Форма отправлена"


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def result(nickname, level, rating):
    return render_template('results.html', nickname=nickname, level=level, rating=rating)


@app.route('/load_photo', methods=['POST', 'GET'])
def file_upload():
    if request.method == 'GET':
        with open('templates/file.html', 'r', encoding='utf-8') as html_stream:
            return html_stream.read()
    elif request.method == 'POST':
        f = request.files['file_name']
        f.save('static/img/' + f.filename)
        return render_template('file.html', file_name=f.filename)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
