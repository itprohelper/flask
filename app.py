# test app

from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/category/')
def showCategories():
    return 'Hola home and category'

@app.route('/test')
def showTest():
    return 'This is a test'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
