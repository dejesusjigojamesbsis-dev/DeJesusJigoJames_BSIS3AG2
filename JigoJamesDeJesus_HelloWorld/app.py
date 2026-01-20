from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return 'Jigo James De Jesus Hello World!'
if __name__ == '__main__':
    app.run(debug=True)