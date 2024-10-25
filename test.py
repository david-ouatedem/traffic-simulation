import requests
import time

# Replace with your app's actual endpoint
url = 'http://localhost:8080'

# Function to generate dummy data for testing
def generate_dummy_data():
    return [
        {
            "route_id": "lane_1",
            "vehicle_count": 5,
            "avg_speed": 15.5,
            "traffic_density": 0.8,
            "timestamp": time.time()
        },
        {
            "route_id": "lane_2",
            "vehicle_count": 3,
            "avg_speed": 10.0,
            "traffic_density": 0.6,
            "timestamp": time.time()
        }
    ]

# Send the dummy data
try:
    dummy_data = generate_dummy_data()
    response = requests.post(url, json=dummy_data)
    
    if response.status_code == 200:
        print("Data sent successfully:", dummy_data)
    else:
        print(f"Failed to send data: {response.status_code} - {response.text}")
except requests.exceptions.RequestException as e:
    print("Error sending data:", e)
