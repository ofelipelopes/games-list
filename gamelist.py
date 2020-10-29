from flask import Flask, render_template

app = Flask(__name__)
@app.route('/inicio')
def inicio():
    return render_template(list.html)

app.run()
