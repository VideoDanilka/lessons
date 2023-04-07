from flask import Flask, render_template


app = Flask(__name__)


@app.route('/index/<Title>/')
def result(Title):
    return render_template('form1.html', Title=Title)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
