from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def resume():
    return render_template('이력서.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
