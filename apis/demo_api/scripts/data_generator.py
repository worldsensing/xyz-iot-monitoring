import random
from datetime import datetime, timezone, timedelta
from time import sleep

import requests

SERVERS = {
    "local": "http://localhost:5001",
    "deploy": "http://localhost:8000/api"
}
SEL_SERVER = "deploy"

DEVICE = {
    "name": "ABC-1001",
    "category": "Inclinometer"
}
SEL_DEVICE = DEVICE

EVENT = {
    "device_name": SEL_DEVICE["name"],
    "value": "AUTOMATICALLY_GATHERED",
    "datetime": "AUTOMATICALLY_GATHERED"
}
SEL_EVENT = EVENT


# Format: 2020-03-24T14:17:12Z
def get_current_date_time():
    now = datetime.now(timezone.utc)
    #now = now - timedelta(minutes=29)
    now = now.replace(microsecond=0)

    return now.isoformat()


def post_info(url, body):
    response = requests.post(url, json=body)
    print(response)


def add_device(device):
    url = f"{SERVERS[SEL_SERVER]}/devices"
    print(f"Adding device to {url}")
    print(device)

    post_info(url, device)


def add_event(event):
    url = f"{SERVERS[SEL_SERVER]}/events"
    print(f"Adding event to {url}")

    # Generates a value from an uniform 0 1, and round it to 4 decimals
    event["value"] = str(round(random.uniform(0, 1), 4))
    event["datetime"] = get_current_date_time()

    print(event)

    post_info(url, event)


if __name__ == "__main__":
    add_device(SEL_DEVICE)
    while True:
        add_event(SEL_EVENT)
        sleep(2)
