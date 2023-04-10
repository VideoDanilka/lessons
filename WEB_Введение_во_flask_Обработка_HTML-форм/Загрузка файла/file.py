from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def file_upload():
    if request.method == 'GET':
        with open('templates/file.html', 'r', encoding='utf-8') as html_stream:
            return html_stream.read()
    elif request.method == 'POST':
        f = request.files['file_name']
        f.save('static/img/' + f.filename)
        return render_template('file.html', file_name=f.file_name)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
