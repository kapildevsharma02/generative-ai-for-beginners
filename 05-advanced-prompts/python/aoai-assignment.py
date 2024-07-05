from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('kapil', 'World')
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run()
