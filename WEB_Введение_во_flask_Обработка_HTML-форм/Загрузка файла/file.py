from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def file_upload():
    if request.method == 'GET':
        with open('templates/file.html', 'r', encoding='utf-8') as html_stream:
            return html_stream.read()
    elif request.method == 'POST':
        file_name = request.form['file_name']
        return render_template('file.html', file_name=file_name)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
