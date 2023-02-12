from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route("/get_location_names", methods=["GET"])
def get_location_names():
    response = jsonify({"locations": util.get_location_names()})
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


@app.route("/predict_home_price", methods=["GET", "POST"])
def predict_home_price():
    Area = float(request.form["Area"])
    location = request.form["location"]
    BHK = int(request.form["BHK"])
    Gymnasium = int(request.form["Gymnasium"])
    Lift_Available = int(request.form["Lift_Available"])
    Car_Parking = int(request.form["Car_Parking"])
    Maintenance_Staff = int(request.form["Maintenance_Staff"])
    Security = int(request.form["Security"])
    Childrens_Play_Area = int(request.form["Childrens_Play_Area"])
    Clubhouse = int(request.form["Clubhouse"])
    Intercom = int(request.form["Intercom"])
    response = jsonify(
        {
            "estimated_price": util.get_estimated_price(
                Area,
                location,
                BHK,
                Gymnasium,
                Lift_Available,
                Car_Parking,
                Maintenance_Staff,
                Security,
                Childrens_Play_Area,
                Clubhouse,
                Intercom,
            )
        }
    )
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()
