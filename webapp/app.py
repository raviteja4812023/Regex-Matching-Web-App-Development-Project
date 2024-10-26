from flask import Flask ,  render_template, request
from flask_cors import CORS
import re


app=Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('home.html')


@app.route("/results",methods=['POST'])
def match_pattern():
    test_string = request.form.get('test_string', '')
    regex_pattern = request.form.get('regex_pattern', '')
    matches = re.findall(regex_pattern, test_string)
    return render_template('result.html', matches=matches)


@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form.get('email', '')
    validation_result = 'Valid Email' if re.match(r'^[\w\.-]+@[\w\.-]+$', email) else 'Invalid Email'
    return render_template('result.html', validation_result=validation_result)


if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000)