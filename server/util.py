import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None


def get_estimated_price(
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
):
    try:
        loc_index = __data_columns.index(location.Upper())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = Area
    x[1] = BHK
    x[2] = Gymnasium
    x[3] = Lift_Available
    x[4] = Car_Parking
    x[5] = Maintenance_Staff
    x[6] = Security
    x[7] = Childrens_Play_Area
    x[8] = Clubhouse
    x[9] = Intercom
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[10:]  # first 3 columns are sqft, bath, bhk

    global __model
    if __model is None:
        with open("./artifacts/mumbai_home_prices_model.pickle", "rb") as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")


def get_location_names():
    return __locations


def get_data_columns():
    return __data_columns


if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price(1245,'Airoli',2,0,1,1,1,1,0,0,0))
