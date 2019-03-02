from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return  render_template('index.html')

@app.route('/bamburi')
def bamburi():
    return '<h1>Hello Bamburi!</h1>'

# @app.route('/town/<name>')
# def town(name):
#     return f'I am in {name}'
    

# @app.route('/latin<latin_name>')
# def latin(latin_name):
#     return'


if __name__ == '__main__':
    app.run(debug=True)
