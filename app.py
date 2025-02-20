from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/about')
def about():
    return render_template('/about.html')

@app.route('/contact')
def contact():
    return render_template('/contact.html')

@app.route('/python')
def py():
    return render_template('/python.html')

@app.route('/data')
def dat():
    return render_template('/data.html')

@app.route('/java')
def jav():
    return render_template('/java.html')

@app.route('/ruby')
def ruby():
    return render_template('/ruby.html')

@app.route('/learn')
def learn():
    return render_template('/learning.html')




if __name__=="__main__":
    app.run(debug = True)