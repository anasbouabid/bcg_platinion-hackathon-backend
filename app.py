from flask import Flask
from flask import request
from flask import jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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
    for i in range(1, len(df_species)):
        if abs(X["temp"]-df_species["Optimal T(°C)"][i]) < min:
            min = abs(X["temp"]-df_species["Optimal T(°C)"][i])
            index = i
            list.append(index)
    return df_species["Microalage Specy"][list[-top:]].tolist()


@app.route("/industries", methods=['GET'])
def industries():
    return jsonify(
        [
            {
                "Industry": "Biofertilizers",
                "Recommended species": ["Arthrospira",	"Aulosira fertilissima ",	"Auxin",	"Charophyceae",	"Chlorella",	"Chlorophyceae",	"Cytokinin",	"Klebsormidium",	"Nannochloris ",	"Nannochloropsis",	"Quadricauda",	"Scenedesmus",	"Spirulina",	"Trebouxiophyceae",	"Ulothrix",	"Ulvophyceae",	"Vulgaris"]
            },
            {
                "Industry": "Cosmetics",
                "Recommended species": ["Astaxanthin",	"Chlorella",	"Dunaliella salina",	"Haematococcus pluvialis",	"Nannochloropsis",	"Nostoc flegelliforme",	"Phaeodactylum tricornutum",	"phycocyanobilins",	"Porphyridium",	"Rhodella",	"Scenedesmus",	"Skeletonema"
                                        ]
            },
            {
                "Industry": "Pharmaceutical",
                "Recommended species": ["Amphidinium",	"Ascophyllum",	"astaxanthin",	"Chlorella",	"Costatum",	"Ecklonia",	"Enteromorpha",	"Flagelliforme",	"Fucus",	"galbana",	"Gigartina",	"Gyrodinium",	"Haematococcus",	"Haematococcus",	"Impudicum",	"Isochrysis",	"Jjaponica",	"Laminaria",	"Linza",	"Navicula directa",	"Nodosum",	"Nostoc",	"Phaeodactylum",	"pinnatifida",	"platensis",	"Pluvialis",	"Porphyridium",	"Skeletonema",	"Skottsbergii",	"Spirulina",	"stolonifera",	"Tetraselmis",	"Tricornutum",	"Ulva rigida",	"Undaria",	"Vesiculosus",	"Vulgaris"]
            }
        ]
    )


@app.route("/species", methods=['GET'])
def species():
    return jsonify(
        [
            {
                "specie": "Amphidinium",
                "params": {
                    "Optimal CO2": 35,
                    "Optimal T": 3,
                    "Optimal ph": 5.7,
                    "N": 487,
                    "P": 12,
                    "Biomass productivity ": 0.922355805546878,
                    "CO2 fixation rate": 0.599819553438134
                }
            },
            {
                "specie": "Arthrospira",
                "params": {
                    "Optimal CO2": 24,
                    "Optimal T": 3,
                    "Optimal ph": 7,
                    "N": 1039,
                    "P": 1067,
                    "Biomass productivity ": 0.451773966320841,
                    "CO2 fixation rate": 0.481166097202644
                }
            },
            {
                "specie": "Ascophyllum",
                "params": {
                    "Optimal CO2": 13,
                    "Optimal T": 10,
                    "Optimal ph": 6.2,
                    "N": 649,
                    "P": 534,
                    "Biomass productivity ": 0.179868294934697,
                    "CO2 fixation rate": 0.946582763070373
                }
            },
            {
                "specie": "Astaxanthin",
                "params": {
                    "Optimal CO2": 61,
                    "Optimal T": 37,
                    "Optimal ph": 7.3,
                    "N": 371,
                    "P": 398,
                    "Biomass productivity ": 0.365207850869609,
                    "CO2 fixation rate": 0.491777484467235
                }
            },
            {
                "specie": "Aulosira fertilissima ",
                "params": {
                    "Optimal CO2": 59,
                    "Optimal T": 27,
                    "Optimal ph": 8.1,
                    "N": 87,
                    "P": 273,
                    "Biomass productivity ": 0.212183870280987,
                    "CO2 fixation rate": 0.895848067431559
                }
            },
            {
                "specie": "Auxin",
                "params": {
                    "Optimal CO2": 64,
                    "Optimal T": 13,
                    "Optimal ph": 5.5,
                    "N": 864,
                    "P": 38,
                    "Biomass productivity ": 0.650025716160749,
                    "CO2 fixation rate": 0.958244708474275
                }
            },
            {
                "specie": "Charophyceae",
                "params": {
                    "Optimal CO2": 65,
                    "Optimal T": 16,
                    "Optimal ph": 4.2,
                    "N": 730,
                    "P": 1045,
                    "Biomass productivity ": 0.0302491027101973,
                    "CO2 fixation rate": 0.698573100062943
                }
            },
            {
                "specie": "Chlorella",
                "params": {
                    "Optimal CO2": 18,
                    "Optimal T": 30,
                    "Optimal ph": 6.4,
                    "N": 34.65,
                    "P": 17.10,
                    "Biomass productivity ": 0.087,
                    "CO2 fixation rate": 0.163
                }
            },
            {
                "specie": "Chlorocum",
                "params": {
                    "Optimal CO2": 40,
                    "Optimal T": 30,
                    "Optimal ph": 5.5,
                    "N": 1250,
                    "P": 1250,
                    "Biomass productivity ": 1,
                    "CO2 fixation rate": 1
                }
            },
            {
                "specie": "Costatum",
                "params": {
                    "Optimal CO2": 4,
                    "Optimal T": 10,
                    "Optimal ph": 5.1,
                    "N": 1100,
                    "P": 1064,
                    "Biomass productivity ": 0.4168996606872,
                    "CO2 fixation rate": 0.993735971344061
                }
            },
            {
                "specie": "Cytokinin",
                "params": {
                    "Optimal CO2": 50,
                    "Optimal T": 28,
                    "Optimal ph": 6.9,
                    "N": 586,
                    "P": 955,
                    "Biomass productivity ": 0.4168996606872,
                    "CO2 fixation rate": 0.304331854112847
                }
            },
            {
                "specie": "Dunaliella salina",
                "params": {
                    "Optimal CO2": 3,
                    "Optimal T": 27,
                    "Optimal ph": 7.3,
                    "N": 1000,
                    "P": 535,
                    "Biomass productivity ": 0.170,
                    "CO2 fixation rate": 0.313
                }
            },
            {
                "specie": "Ecklonia",
                "params": {
                    "Optimal CO2": 52,
                    "Optimal T": 20,
                    "Optimal ph": 6,
                    "N": 836,
                    "P": 870,
                    "Biomass productivity ": 0.469355619610648,
                    "CO2 fixation rate": 0.307689457894944
                }
            },
            {
                "specie": "Enteromorpha",
                "params": {
                    "Optimal CO2": 13,
                    "Optimal T": 25,
                    "Optimal ph": 5.4,
                    "N": 910,
                    "P": 379,
                    "Biomass productivity ": 0.164130941508297,
                    "CO2 fixation rate": 0.96453578714873
                }
            },
            {
                "specie": "Fucus",
                "params": {
                    "Optimal CO2": 59,
                    "Optimal T": 27,
                    "Optimal ph": 7,
                    "N": 1200,
                    "P": 2870,
                    "Biomass productivity ": 0.811941904867667,
                    "CO2 fixation rate": 0.75947164090374
                }
            },
            {
                "specie": "galbana",
                "params": {
                    "Optimal CO2": 41,
                    "Optimal T": 38,
                    "Optimal ph": 2,
                    "N": 1100,
                    "P": 873,
                    "Biomass productivity ": 0.134924521057151,
                    "CO2 fixation rate": 0.371628277345356
                }
            },
            {
                "specie": "Gigartina",
                "params": {
                    "Optimal CO2": 16,
                    "Optimal T": 9,
                    "Optimal ph": 8.3,
                    "N": 174,
                    "P": 37,
                    "Biomass productivity ": 0.22679738467196,
                    "CO2 fixation rate": 0.696421681208586
                }
            },
            {
                "specie": "Gyrodinium",
                "params": {
                    "Optimal CO2": 18,
                    "Optimal T": 26,
                    "Optimal ph": 8.51,
                    "N": 20,
                    "P": 17,
                    "Biomass productivity ": 0.243275261093587,
                    "CO2 fixation rate": 0.0971586084847468
                }
            },
            {
                "specie": "Haematococcus",
                "params": {
                    "Optimal CO2": 37,
                    "Optimal T": 21,
                    "Optimal ph": 6.5,
                    "N": 96,
                    "P": 87,
                    "Biomass productivity ": 0.886981491994113,
                    "CO2 fixation rate": 0.170272372388912
                }
            },
            {
                "specie": "Impudicum",
                "params": {
                    "Optimal CO2": 34,
                    "Optimal T": 20,
                    "Optimal ph": 5.9,
                    "N": 421,
                    "P": 378,
                    "Biomass productivity ": 0.076,
                    "CO2 fixation rate": 0.143
                }
            },
            {
                "specie": "Isochrysis",
                "params": {
                    "Optimal CO2": 54,
                    "Optimal T": 11,
                    "Optimal ph": 7.4,
                    "N": 249,
                    "P": 179,
                    "Biomass productivity ": 0.566806793606053,
                    "CO2 fixation rate": 0.332782410307501
                }
            },
            {
                "specie": "Jjaponica",
                "params": {
                    "Optimal CO2": 24,
                    "Optimal T": 16,
                    "Optimal ph": 4.4,
                    "N": 120,
                    "P": 1037,
                    "Biomass productivity ": 0.978490374271464,
                    "CO2 fixation rate": 0.790712918836618
                }
            },
            {
                "specie": "Gigartina",
                "params": {
                    "Optimal CO2": 65,
                    "Optimal T": 12,
                    "Optimal ph": 7.7,
                    "N": 87,
                    "P": 37,
                    "Biomass productivity ": 0.868103675251021,
                    "CO2 fixation rate": 0.960028528898843
                }
            },
            {
                "specie": "Klebsormidium",
                "params": {
                    "Optimal CO2": 44,
                    "Optimal T": 17,
                    "Optimal ph": 6.9,
                    "N": 61,
                    "P": 910,
                    "Biomass productivity ": 0.958751297951996,
                    "CO2 fixation rate": 0.521212408820485
                }
            },
            {
                "specie": "Laminaria",
                "params": {
                    "Optimal CO2": 27,
                    "Optimal T": 37,
                    "Optimal ph": 7.9,
                    "N": 70,
                    "P": 28,
                    "Biomass productivity ": 0.64310419282317,
                    "CO2 fixation rate": 0.799141682551272
                }
            },
            {
                "specie": "Linza",
                "params": {
                    "Optimal CO2": 11,
                    "Optimal T": 24,
                    "Optimal ph": 5.5,
                    "N": 36,
                    "P": 32,
                    "Biomass productivity ": 0.363624421256501,
                    "CO2 fixation rate": 0.70446381840858
                }
            },
            {
                "specie": "Nannochloris ",
                "params": {
                    "Optimal CO2": 15,
                    "Optimal T": 21,
                    "Optimal ph": 8.6,
                    "N": 871,
                    "P": 580,
                    "Biomass productivity ": 0.239691235833377,
                    "CO2 fixation rate": 0.343285341968303
                }
            },
            {
                "specie": "Nannochloropsis",
                "params": {
                    "Optimal CO2": 10,
                    "Optimal T": 21,
                    "Optimal ph": 7.7,
                    "N": 13,
                    "P": 39,
                    "Biomass productivity ": 0.521255623887383,
                    "CO2 fixation rate": 0.122607374293389
                }
            },
            {
                "specie": "Navicula directa",
                "params": {
                    "Optimal CO2": 23,
                    "Optimal T": 19,
                    "Optimal ph": 8.51,
                    "N": 1180,
                    "P": 1800,
                    "Biomass productivity ": 0.439229980860403,
                    "CO2 fixation rate": 0.475162185331856
                }
            },
            {
                "specie": "Nodosum",
                "params": {
                    "Optimal CO2": 62,
                    "Optimal T": 30,
                    "Optimal ph": 7.7,
                    "N": 349,
                    "P": 18,
                    "Biomass productivity ": 0.32614900191314,
                    "CO2 fixation rate": 0.109532470472668
                }
            },
            {
                "specie": "Nostoc",
                "params": {
                    "Optimal CO2": 8,
                    "Optimal T": 26,
                    "Optimal ph": 4.76,
                    "N": 397,
                    "P": 238,
                    "Biomass productivity ": 0.804450216393125,
                    "CO2 fixation rate": 0.933917409351522
                }
            },
            {
                "specie": "Phaeodactylum",
                "params": {
                    "Optimal CO2": 42,
                    "Optimal T": 3,
                    "Optimal ph": 5.9,
                    "N": 409,
                    "P": 680,
                    "Biomass productivity ": 0.510064037450006,
                    "CO2 fixation rate": 0.0943149997412173
                }
            },
            {
                "specie": "Phycocyanobilins",
                "params": {
                    "Optimal CO2": 60,
                    "Optimal T": 29,
                    "Optimal ph": 6,
                    "N": 317,
                    "P": 367,
                    "Biomass productivity ": 0.44239142807891,
                    "CO2 fixation rate": 0.907299808208069
                }
            },
            {
                "specie": "Pinnatifida",
                "params": {
                    "Optimal CO2": 62,
                    "Optimal T": 24,
                    "Optimal ph": 5.2,
                    "N": 287,
                    "P": 127,
                    "Biomass productivity ": 0.585082388896373,
                    "CO2 fixation rate": 0.338847633803597
                }
            },
            {
                "specie": "Platensis",
                "params": {
                    "Optimal CO2": 11,
                    "Optimal T": 17,
                    "Optimal ph": 4.9,
                    "N": 961,
                    "P": 71,
                    "Biomass productivity ": 0.804198390810289,
                    "CO2 fixation rate": 0.995484068761378
                }
            },
            {
                "specie": "Pluvialis",
                "params": {
                    "Optimal CO2": 4,
                    "Optimal T": 9,
                    "Optimal ph": 7,
                    "N": 49,
                    "P": 729,
                    "Biomass productivity ": 0.0476107847952451,
                    "CO2 fixation rate": 0.92969445387957
                }
            },
            {
                "specie": "Porphyridium",
                "params": {
                    "Optimal CO2": 24,
                    "Optimal T": 7,
                    "Optimal ph": 7.3,
                    "N": 489,
                    "P": 687,
                    "Biomass productivity ": 0.17115119643798,
                    "CO2 fixation rate": 0.642223776456338
                }
            },
            {
                "specie": "Quadricauda",
                "params": {
                    "Optimal CO2": 40,
                    "Optimal T": 16,
                    "Optimal ph": 5.7,
                    "N": 1370,
                    "P": 1200,
                    "Biomass productivity ": 0.717916812365694,
                    "CO2 fixation rate": 0.631344014051725
                }
            },
            {
                "specie": "Rhodella",
                "params": {
                    "Optimal CO2": 5,
                    "Optimal T": 19,
                    "Optimal ph": 6.9,
                    "N": 279,
                    "P": 286,
                    "Biomass productivity ": 0.3374141222852,
                    "CO2 fixation rate": 0.307060732294659
                }
            },
            {
                "specie": "Scenedesmus",
                "params": {
                    "Optimal CO2": 1,
                    "Optimal T": 17,
                    "Optimal ph": 5.1,
                    "N": 51.66,
                    "P": 4.46,
                    "Biomass productivity ": 0.009,
                    "CO2 fixation rate": 0.016
                }
            },
            {
                "specie": "Skeletonema",
                "params": {
                    "Optimal CO2": 42,
                    "Optimal T": 15,
                    "Optimal ph": 4.9,
                    "N": 604,
                    "P": 549,
                    "Biomass productivity ": 0.120553640391222,
                    "CO2 fixation rate": 0.145355223889303
                }
            },
            {
                "specie": "Skottsbergii",
                "params": {
                    "Optimal CO2": 36,
                    "Optimal T": 7,
                    "Optimal ph": 8,
                    "N": 340,
                    "P": 78,
                    "Biomass productivity ": 0.27946595464238,
                    "CO2 fixation rate": 0.253958781265985
                }
            },
            {
                "specie": "Spirulina",
                "params": {
                    "Optimal CO2": 12,
                    "Optimal T": 30,
                    "Optimal ph": 7,
                    "N": 173.27,
                    "P": 284.93,
                    "Biomass productivity ": 0.220,
                    "CO2 fixation rate": 0.413
                }
            },
            {
                "specie": "Stolonifera",
                "params": {
                    "Optimal CO2": 31,
                    "Optimal T": 27,
                    "Optimal ph": 6.7,
                    "N": 30,
                    "P": 23,
                    "Biomass productivity ": 0.495243436037669,
                    "CO2 fixation rate": 0.687463266655029
                }
            },
            {
                "specie": "Tetraselmis",
                "params": {
                    "Optimal CO2": 15,
                    "Optimal T": 8,
                    "Optimal ph": 5.8,
                    "N": 347,
                    "P": 451,
                    "Biomass productivity ": 0.636068088312682,
                    "CO2 fixation rate": 0.603093984982543
                }
            },
            {
                "specie": "Trebouxiophyceae",
                "params": {
                    "Optimal CO2": 68,
                    "Optimal T": 8,
                    "Optimal ph": 5.6,
                    "N": 65,
                    "P": 89,
                    "Biomass productivity ": 0.444240904210525,
                    "CO2 fixation rate": 0.728176669282192
                }
            },
            {
                "specie": "Tricornutum",
                "params": {
                    "Optimal CO2": 55,
                    "Optimal T": 30,
                    "Optimal ph": 7.9,
                    "N": 79,
                    "P": 47,
                    "Biomass productivity ": 0.579069187464778,
                    "CO2 fixation rate": 0.548434278353662
                }
            },
            {
                "specie": "Ulothrix",
                "params": {
                    "Optimal CO2": 8,
                    "Optimal T": 12,
                    "Optimal ph": 5.8,
                    "N": 1170,
                    "P": 1800,
                    "Biomass productivity ": 0.332679121516051,
                    "CO2 fixation rate": 0.880508554156655
                }
            },
            {
                "specie": "Ulva rigida",
                "params": {
                    "Optimal CO2": 20,
                    "Optimal T": 31,
                    "Optimal ph": 7.2,
                    "N": 48,
                    "P": 65,
                    "Biomass productivity ": 0.959040428917005,
                    "CO2 fixation rate": 0.432835287742658
                }
            },
            {
                "specie": "Ulvophyceae",
                "params": {
                    "Optimal CO2": 20,
                    "Optimal T": 7,
                    "Optimal ph": 5,
                    "N": 1087,
                    "P": 1200,
                    "Biomass productivity ": 0.975917628551852,
                    "CO2 fixation rate": 0.273435409574303
                }
            },
            {
                "specie": "Undaria",
                "params": {
                    "Optimal CO2": 32,
                    "Optimal T": 31,
                    "Optimal ph": 7.7,
                    "N": 680,
                    "P": 587,
                    "Biomass productivity ": 0.987242614067247,
                    "CO2 fixation rate": 0.735074692543048
                }
            },
            {
                "specie": "Vesiculosus",
                "params": {
                    "Optimal CO2": 9,
                    "Optimal T": 26,
                    "Optimal ph": 8.1,
                    "N": 242,
                    "P": 263,
                    "Biomass productivity ": 0.469636004807061,
                    "CO2 fixation rate": 0.648047387339154
                }
            },
            {
                "specie": "Vulgaris",
                "params": {
                    "Optimal CO2": 1,
                    "Optimal T": 18,
                    "Optimal ph": 6.1,
                    "N": 409,
                    "P": 680,
                    "Biomass productivity ": 0.523712262349636,
                    "CO2 fixation rate": 0.457705880700398
                }
            }
        ]
    )
