from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    # Grab file name from user input
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    df.columns = [col.strip() for col in df.columns] # remove unnecessary whitespace from columns
    # Grab temperature. (divide by 10 is to move decimal to proper place.)
    temperature = df.loc[df['DATE'] == date]['TG'].squeeze() / 10
    return {"station": station,
            "date": date,
            "temperature": temperature}


if __name__ == "__main__":
    app.run(debug=True)

