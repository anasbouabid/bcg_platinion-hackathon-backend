from flask import Flask
from flask import request
import pandas as pd

app = Flask(__name__)

df_species = pd.read_csv("industry_species.csv")

@app.route("/")
def hello_world():
    
    return "Hello, World!"


# X = {"temp": 30, "humidity": 5, "pressure": 6}

@app.route("/test", methods=['POST'])
def recommender():
    X = request.json
    top = 3
    min = abs(X["temp"] - df_species["Optimal T(°C)"][0])
    index = 0
    list = []
    for i in range(1,len(df_species)):
        if abs(X["temp"]-df_species["Optimal T(°C)"][i]) < min:
            min= abs(X["temp"]-df_species["Optimal T(°C)"][i])
            index = i
            list.append(index)
    return df_species["Microalage Specy"][list[-top:]].tolist()