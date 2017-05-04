from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/request-counter', methods=['GET'])
def request_counter_get():
    return type(methods)


@app.route('/request-counter', methods=['POST'])
def request_counter_post():
    pass


@app.route('/statistics ', methods=['GET'])
def request_counter_statistics():
    pass


if __name__ == '__main__':
    app.run(debug=True)
