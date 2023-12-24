import warnings

warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


df = pd.read_csv("fake_flood_data.csv")

input_data = df[
    ["Temperature", "Humidity", "Precipitation", "RoadOne", "RoadTwo", "RoadThree"]
]
output_data = df[["FloodToday"]]

input_scaler = preprocessing.MinMaxScaler()
input_scaler.fit(input_data)
input_scaled = pd.DataFrame(
    input_scaler.transform(input_data),
    index=input_data.index,
    columns=input_data.columns,
)

output_scaler = preprocessing.MinMaxScaler()
output_scaler.fit(output_data)
output_scaled = pd.DataFrame(
    output_scaler.transform(output_data),
    index=output_data.index,
    columns=output_data.columns,
)

input_train, input_test, output_train, output_test = train_test_split(
    input_scaled, output_scaled, test_size=0.25
)

classifier_logreg = LogisticRegression(random_state=0)
classifier_logreg.fit(input_train, output_train.values.ravel())

output_prediction = classifier_logreg.predict(input_test)
score = accuracy_score(output_test, output_prediction)

print(f"accuracy using logistic regression is: {score}")


while True:
    new_data = input("Enter new flood data:")
    flood_data = new_data.split(",")
    flood_data = np.array([flood_data])

    scaled_flood_data = input_scaler.transform(flood_data)
    probability = classifier_logreg.predict_proba(scaled_flood_data)
    flood_probability = int(probability[0][1] * 100)

    print(f"Probability of flood: {flood_probability} %")
