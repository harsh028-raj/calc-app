# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Calculator API is live! Use the /calc endpoint with GET parameters.'

@app.route('/calc', methods=['GET'])
def calculate():
    op = request.args.get('op')
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))

    if op == 'add':
        result = a + b
    elif op == 'sub':
        result = a - b
    elif op == 'mul':
        result = a * b
    elif op == 'div':
        result = a / b
    else:
        return jsonify({'error': 'Invalid operation'}), 400

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
