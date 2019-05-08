import json

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/simple-graph")
def simple_graph():
    return render_template("simple-graph.html")

@app.route("/simple-graph-2")
def simple_graph_2():
    return render_template("simple-graph-2.html")

@app.route("/simple-scatter")
def simple_scatter():
    return render_template("simple-scatter.html")

if __name__ == "__main__":
    app.run(debug=True)
