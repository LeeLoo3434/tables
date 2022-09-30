from flask import Flask, render_template
from allthebros import bros
app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', people= bros)

if __name__=='__main__':
    app.run(debug=True, host='localhost', port=5000)