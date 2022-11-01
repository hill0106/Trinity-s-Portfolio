from flask import *

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Resume.html')
def resume():
    return render_template('Resume.html')


@app.route('/Project.html')
def project():
    return render_template('Project.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True, port=5000)