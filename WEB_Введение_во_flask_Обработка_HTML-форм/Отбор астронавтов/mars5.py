from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        with open('form.html', 'r', encoding='utf-8') as html_stream:
            return html_stream.read()
    elif request.method == 'POST':
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

