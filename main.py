import test

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    test.open()
    x = test.browse()
    test.close()
    return 'Hello, World! ' + str(x)


if __name__ =='__main__':
    app.run(host='0.0.0.0')


