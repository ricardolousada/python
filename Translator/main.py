from flask import Flask, render_template
import pandas as pd

data = pd.read_csv("dictionary.csv")
app = Flask("__name__")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<word>")
def about(word):
    definition = data.loc[data["word"] == word]["definition"].squeeze()
    definition = definition.strip("\n")
    return {"defenition": definition,
            "word": word}

if __name__ == "__main__":
    #line to change the port and run the app, port is optinal
    app.run(debug=True, port = 5001)

