from flask import Flask, render_template
import getgraph as gg

app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Welcome to TutsPlus!"
    
@app.route('/showLineChart')
def line():
    graphJSON = gg.get_graph()
    return render_template('index.html',graphJSON=graphJSON)