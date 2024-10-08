import os
import json
from helpers.logger import logger

class StateMachine:
    STATE_FILE = 'ip.json'
    STATE_MACHINE_IP_KEY = 'ipv4'

    def __init__(self):
        self.current_state = self.load_state()
        self.current_ip = self.current_state.get(self.STATE_MACHINE_IP_KEY, None)

    def load_state(self):
        if os.path.exists(self.STATE_FILE):
            with open(self.STATE_FILE, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    logger.error("Failed to decode state file, resetting state.")
                    return {}
        return {}

    def update_state(self, ip_address):
        state = {
            self.STATE_MACHINE_IP_KEY: ip_address
        }

        logger.debug(f"ip_address set to {ip_address}")
        with open(self.STATE_FILE, 'w') as file:
            json.dump(state, file)
