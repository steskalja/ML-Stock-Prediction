from flask import Flask, render_template, request
import getgraph as gg

app = Flask(__name__)
 
@app.route("/", methods =["GET", "POST"])
def cg():
    graphJSON = gg.get_graph()
    if request.method == "POST":
        ntp = request.form.get("num")
        predictJSON = gg.create_predict(int(ntp))
        return render_template('index.html',graphJSON=graphJSON,predictJSON=predictJSON )
    return render_template('index.html',graphJSON=graphJSON)

@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=False)