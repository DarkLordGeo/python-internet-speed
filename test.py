import speedtest
import json
from time import gmtime, strftime
def speed_data():
    st = speedtest.Speedtest()
    task_completed = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    obj = {
        "date": task_completed,
        "download": round(st.download() / 1_000_000, 2),
        "upload": round(st.upload() / 1_000_000, 2),
    }
    try:
        with open("data.json", "r") as r:
            data = json.load(r)
            if not isinstance(data, list):
                data = []
    except FileNotFoundError:
        data = []
    data.append(obj)
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
        print("appended successfully")
speed_data()
