# coding=utf-8
# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#import urllib
#import urllib2
import requests
import json

url = "http://192.168.1.160/power_manager/config"
payload = {
    "enabled": True,
    "phase_switching_mode": 1,
    "excess_charging_enable": False,
    "default_mode": 1,
    "meter_slot_grid_power": 1,
    "target_power_from_grid": 0,
    "guaranteed_power": 1380,
    "cloud_filter_mode": 2
}

headers = {'Content-Type': 'application/json'}

try:
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
