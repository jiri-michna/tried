from flask import Flask, render_template, request
from waitress import serve
from manga import iwonder

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/manga')
def get_manga():
    n = int(request.args.get("n"))
    res = iwonder(n)
    return render_template(
        "manga.html",
        title = res
    )  
@app.route('/mango')
def gheto_manga():
    n = int(request.args.get("n"))
    res = iwonder(n)
    return render_template(
        "mango.html",
        title = res
    )  

if __name__ == "__main__":
    serve(app, host="127.0.0.1", port=8080)
