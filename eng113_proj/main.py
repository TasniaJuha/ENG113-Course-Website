from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/index2')
def index2():
    return render_template('index2.html')

@app.route('/index3')
def index3():
    return render_template('index3.html')
if __name__ == '__main__':
    app.add_url_rule('/index.html', '/index', index)
    app.add_url_rule('/index1.html', '/', home)
    app.add_url_rule('/index2.html', '/index2', index2)
    app.add_url_rule('/index3.html', '/index3', index3)

    app.run(debug=True, port=5001)

'''
@app.route("/")
@app.route("/index")
def home():
    return render_template('index.html')'''
##app.add_url_rule('/index.html', '/', home)