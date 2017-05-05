from flask import Flask, render_template, redirect, url_for, request
import os

dir_path = os.path.dirname(os.path.realpath('request_counts.txt'))

app = Flask(__name__)

counts = {'GET': 0, 'POST': 0, 'DELETE': 0, 'PUT': 0}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/request-counter', methods=['GET'])
def request_counter_get():
    req_method = request.method
    if req_method:
        global counts
        counts['GET'] += 1
    return render_template('request_counter.html', req_method=req_method, counts=counts)


@app.route('/request-counter', methods=['POST'])
def request_counter_post():
    req_method = request.method
    if req_method:
        global counts
        counts['POST'] += 1
    return render_template('request_counter.html', req_method=req_method, counts=counts)


@app.route('/statistics ', methods=['GET'])
def request_counter_statistics():
    return render_template('statistics.html', req_method=req_method)


if __name__ == '__main__':
    app.run(debug=True)
