import argparse
import random
from datetime import datetime, timedelta

import pandas as pd

parser = argparse.ArgumentParser(description="Set constants for data generation")
parser.add_argument("--days", type=int, default=7, help="Number of days to generate")
parser.add_argument(
    "--flood_prob", type=int, default=20, help="Probability of flooding (in percentage)"
)
args = parser.parse_args()

DAYS_TO_GENERATE = args.days
FLOOD_PROBABILITY = args.flood_prob


def generate_flood_probability():
    return True if random.randint(0, 100) < FLOOD_PROBABILITY else False


# in Celsius
def generate_random_temperature(flooding):
    return random.randint(20, 35) if not flooding else random.randint(10, 25)


# in percent
def generate_random_humidity(flooding):
    return random.randint(40, 80) if not flooding else random.randint(60, 90)


# in mm
def generate_random_precipitation(flooding):
    return (
        round(random.uniform(0, 10), 2)
        if not flooding
        else round(random.uniform(5, 50), 2)
    )


# in cm
def generate_random_ultrasonic(flooding):
    return random.randint(0, 20) if not flooding else random.randint(10, 30)


def generate_flood_data():
    today_date = datetime.today()

    data = []
    for i in range(DAYS_TO_GENERATE):
        date = (today_date - timedelta(days=i)).strftime("%Y-%m-%d")
        flood_today = generate_flood_probability()

        temperature = generate_random_temperature(flood_today)
        humidity = generate_random_humidity(flood_today)
        precipitation = generate_random_precipitation(flood_today)
        road1 = generate_random_ultrasonic(flood_today)
        road2 = generate_random_ultrasonic(flood_today)
        road3 = generate_random_ultrasonic(flood_today)

        data.append(
            {
                "Date": date,
                "Temperature": temperature,
                "Humidity": humidity,
                "Precipitation": precipitation,
                "RoadOne": road1,
                "RoadTwo": road2,
                "RoadThree": road3,
                "FloodToday": flood_today,
            }
        )

    df = pd.DataFrame(data)
    df.to_csv("fake_flood_data.csv", index=False)


if __name__ == "__main__":
    generate_flood_data()
