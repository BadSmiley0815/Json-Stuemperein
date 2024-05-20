# coding: utf-8
import requests
import json

##!!!!##################################################################################################
#### Own written code can be placed above this commentblock . Do not change or delete commentblock! ####
########################################################################################################
##** Code created by generator - DO NOT CHANGE! **##

class Warp3_Phase19001(hsl20_4.BaseModule):

    def __init__(self, homeserver_context):
        hsl20_4.BaseModule.__init__(self, homeserver_context, "Warp3")
        self.FRAMEWORK = self._get_framework()
        self.LOGGER = self._get_logger(hsl20_4.LOGGING_NONE,())
        self.PIN_I_IP_WALLBOX=1
        self.PIN_I_TRIGGER_1P=2
        self.PIN_I_TRIGGER_3P=3
        self.PIN_O_DEBUG=1

########################################################################################################
#### Own written code can be placed after this commentblock . Do not change or delete commentblock! ####
###################################################################################################!!!##


    def on_input_value(self, index, value):
        if index == self.PIN_I_TRIGGER_1P:
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
            self.set_output_value(self.PIN_O_DEBUG, response)

        if index == self.PIN_I_TRIGGER_3P:
            url = "http://192.168.1.160/power_manager/config"
            payload = {
                "enabled": True,
                "phase_switching_mode": 2,
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
            self.set_output_value(self.PIN_O_DEBUG, response)



