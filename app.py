from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)