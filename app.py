from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/xz4yamgs/acc_creation')
def acc_creation():
    return render_template('acc_creation.html')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')