import paho.mqtt.client as mqtt
import time
import json
import random

client = mqtt.Client()
client.connect("localhost", 1883, 60)

def generate_vitals():
    temperature = round(random.uniform(34.0, 39.0), 1)
    heart_rate = random.randint(55, 110)
    systolic = random.randint(85, 160)
    diastolic = random.randint(55, 100)
    return [temperature, heart_rate, systolic, diastolic]

while True:
    vitals = generate_vitals()
    payload = json.dumps(vitals)
    client.publish("health/vitals", payload)
    print("Published:", vitals)
    time.sleep(2)

