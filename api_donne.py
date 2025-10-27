#API to take the data for every 10 minutes


import requests
from datetime import datetime, timedelta
import time
import os
import pandas as pd



def coletc_e_append_velib():
    url = "https://opendata.paris.fr/api/records/1.0/search/"
    params = {
        "dataset": "velib-disponibilite-en-temps-reel",
        "rows": 1500
    }
    response = requests.get(url, params=params)
    data = response.json()

    records = [r['fields'] for r in data['records']]
    df = pd.DataFrame(records)

    # Add timestamp
    df['timestamp_coleta'] = datetime.now()

    # Append
    df.to_csv("velib_history.csv", mode='a', header=not os.path.exists("velib_history.csv"), index=False)
    print("Data add to velib_history.csv")

while True:
    coletc_e_append_velib()
    time.sleep(600)  # 10 min
