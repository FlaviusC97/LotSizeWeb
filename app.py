from flask import Flask, render_template, request
import os
app = Flask(__name__)

# Datele tale din tabel
forex_data = {
    "EURUSD": {"price": 1.1314, "lot_size": 0.88},
    "GBPUSD": {"price": 1.32338, "lot_size": 0.76},
    "USDJPY": {"price": 142.855, "lot_size": 0.77},
    "USDCAD": {"price": 1.3913, "lot_size": 0.72},
    "USDCHF": {"price": 0.81814, "lot_size": 1.22},
    "AUDUSD": {"price": 0.63684, "lot_size": 1.57},
    "NZDUSD": {"price": 0.593, "lot_size": 1.69},
    "EURJPY": {"price": 161.666, "lot_size": 0.68},
    "EURGBP": {"price": 0.85512, "lot_size": 1.17},
    "EURCAD": {"price": 1.57478, "lot_size": 0.64},
    "EURCHF": {"price": 0.9254, "lot_size": 1.08},
    "EURAUD": {"price": 1.7789, "lot_size": 0.56},
    "EURNZD": {"price": 1.9095, "lot_size": 0.52},
    "GBPJPY": {"price": 188.996, "lot_size": 0.58},
    "GBPCAD": {"price": 1.84202, "lot_size": 0.54},
    "GBPCHF": {"price": 1.08184, "lot_size": 0.92},
    "GBPAUD": {"price": 2.07966, "lot_size": 0.48},
    "GBPNZD": {"price": 2.23254, "lot_size": 0.45},
    "AUDJPY": {"price": 90.908, "lot_size": 1.20},
    "AUDCAD": {"price": 0.88612, "lot_size": 1.13},
    "AUDNZD": {"price": 1.07416, "lot_size": 0.93},
    "AUDCHF": {"price": 0.5208, "lot_size": 1.92},
    "NZDCAD": {"price": 0.82479, "lot_size": 1.21},
    "NZDJPY": {"price": 84.655, "lot_size": 1.29},
    "NZDCHF": {"price": 0.48506, "lot_size": 2.06},
    "CADJPY": {"price": 102.672, "lot_size": 1.07},
    "CADCHF": {"price": 0.58797, "lot_size": 1.70},
    "CHFJPY": {"price": 174.572, "lot_size": 0.63}
}

@app.route("/", methods=["GET", "POST"])
def index():
    selected = None
    result = None
    amount = 100  # default value

    if request.method == "POST":
        selected = request.form["pair"]
        amount = float(request.form["amount"])
        base_lot = forex_data[selected]["lot_size"]
        result = round(base_lot * (amount / 100), 2)

    return render_template("index.html", forex_data=forex_data, selected=selected, result=result, amount=amount)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render setează PORT
    app.run(host="0.0.0.0", port=port)



