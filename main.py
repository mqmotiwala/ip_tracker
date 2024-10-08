import requests
from helpers.logger import logger
from helpers.pushover import Pushover
from state_machine import StateMachine

IP_URL = 'https://ipv4.icanhazip.com'
ERROR_MSG = 'Error fetching public IP.'

def main():
    def refresh_ip():
        try:
            response = requests.get(IP_URL)
            response.raise_for_status()
            return response.text.strip()

        except requests.RequestException:
            logger.exception(ERROR_MSG)
            return None

    p = Pushover()
    sm = StateMachine()

    refreshed_ip = refresh_ip()
    if refreshed_ip:
        if refreshed_ip != sm.current_ip:
            notif_msg = f"Public IPv4 address changed from {sm.current_ip} to {refreshed_ip}"
            logger.info(notif_msg)
            p.send_notification(notif_msg)
            sm.update_state(refreshed_ip)
        else:
            notif_msg = f"Public IPv4 address is still {refreshed_ip}"
            logger.info(notif_msg)
            p.send_notification(notif_msg, priority=-2, is_log=True)
    else:
        p.send_notification(ERROR_MSG, is_log=True)

if __name__ == '__main__':
    main()