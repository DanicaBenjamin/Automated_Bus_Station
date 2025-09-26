import requests
import json
import random
import time

THINGSBOARD_HOST = "thingsboard.cloud"
ACCESS_TOKEN = "OwENJUaR49ynzgPAfj20"  

url = f"https://{THINGSBOARD_HOST}/api/v1/{ACCESS_TOKEN}/telemetry"

print("🚀 Starting telemetry upload... Press Ctrl+C to stop.")

while True:
    data = {
        "temperature": random.randint(20, 35),
        "humidity": random.randint(30, 80),
        "passenger_count": random.randint(0, 50),
        "bus_capacity": 50
    }

    try:
        response = requests.post(
            url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data),
            timeout=5
        )

        if response.status_code == 200:
            print("✅ Sent:", data)
        else:
            print("❌ Failed:", response.status_code, response.text)

    except Exception as e:
        print("⚠️ Error:", e)

    time.sleep(5)  
import requests
import json
import random
import time

THINGSBOARD_HOST = "thingsboard.cloud"
ACCESS_TOKEN = "OwENJUaR49ynzgPAfj20"  

url = f"https://{THINGSBOARD_HOST}/api/v1/{ACCESS_TOKEN}/telemetry"

print("🚀 Starting telemetry upload... Press Ctrl+C to stop.")

while True:
    data = {
        "temperature": random.randint(20, 35),
        "humidity": random.randint(30, 80),
        "passenger_count": random.randint(0, 50),
        "bus_capacity": 50
    }

    try:
        response = requests.post(
            url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data),
            timeout=5
        )

        if response.status_code == 200:
            print("✅ Sent:", data)
        else:
            print("❌ Failed:", response.status_code, response.text)

    except Exception as e:
        print("⚠️ Error:", e)

    time.sleep(5)  
import requests
import json
import random
import time

THINGSBOARD_HOST = "thingsboard.cloud"
ACCESS_TOKEN = "OwENJUaR49ynzgPAfj20"  

url = f"https://{THINGSBOARD_HOST}/api/v1/{ACCESS_TOKEN}/telemetry"

print("🚀 Starting telemetry upload... Press Ctrl+C to stop.")

while True:
    data = {
        "temperature": random.randint(20, 35),
        "humidity": random.randint(30, 80),
        "passenger_count": random.randint(0, 50),
        "bus_capacity": 50
    }

    try:
        response = requests.post(
            url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data),
            timeout=5
        )

        if response.status_code == 200:
            print("✅ Sent:", data)
        else:
            print("❌ Failed:", response.status_code, response.text)

    except Exception as e:
        print("⚠️ Error:", e)

    time.sleep(5)  
