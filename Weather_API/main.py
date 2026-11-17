from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID","STANAME                                 "]]

@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    # Dynamically build file path matching the weather station code format
    filename = f"data_small/TG_STAID{str(station).zfill(6)}.txt"
    # Read the text file, ignoring metadata comments (first 20 rows)
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    # Extract the exact temperature matching the string date and convert to a native type
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
    return { "station": station,
        "date": date,
        "temperature": int(temperature) / 10,
    }
@app.route("/api/v1/<station>")
def all_data(station):
    filename = f"data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict(orient="records")
    return result

@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station, year):
    filename = f"data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20,)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))].to_dict(
        orient="records"
    )
    return result


if __name__ == "__main__":
    app.run(debug=True, port=5000)