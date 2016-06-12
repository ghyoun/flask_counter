from flask import Flask, render_template, request, session
app = Flask(__name__)
app.secret_key = "secretKey"

@app.route('/', methods=['POST'])
def counter():
    try:
        session['count'] += 1
    except KeyError:
        session['count'] = 1


    return render_template('index.html', count=session['count'])
app.run(debug=True)
