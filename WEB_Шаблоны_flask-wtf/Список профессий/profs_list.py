import json

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/list_prof/ol')
def ol():
    with open("profs.json", "rt", encoding="utf8") as f:
        list_prof = json.loads(f.read())
    return render_template('form1.html', profs=list_prof)


@app.route('/list_prof/ul')
def ul():
    with open("profs.json", "rt", encoding="utf8") as f:
        list_prof = json.loads(f.read())
    return render_template('form2.html', profs=list_prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
