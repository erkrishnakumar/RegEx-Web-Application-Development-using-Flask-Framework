import re
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/regex_result', methods=['POST'])
def regex_result():
    pattern = request.form['pattern']
    text = request.form['text']
    print(pattern)
    matches = re.findall(rf"{pattern}", text)
    return render_template('index.html',pattern=pattern,text=text,matches=matches)
    
@app.route('/email')
def index1():
    return render_template('results.html',valid_mail=None)

@app.route('/validate_email', methods=['POST'])
def validate_email():
    pattern =r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+[.][\w]{2,3}$"
    text = request.form['mail']
    mails= re.findall(pattern, text)
    if mails!=[]:
        return render_template('results.html', valid_mail=True,text=text)
    else:
        return render_template('results.html', valid_mail=False,text=text)

if __name__ == '__main__':
    app.run(debug=True, host = "0.0.0.0")
