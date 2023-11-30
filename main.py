from flask import Flask, render_template
import pandas

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<stations>/<date>")
def about(station, date):
    df = pandas.read_csv(" ")
    temperature = df.station(date)
    return {"station": station,
            "date": date,
            "temperature": temperature}


if __name__ == "  main  ":
    app.run(debug=True)
