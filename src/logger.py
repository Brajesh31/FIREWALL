import logging
from datetime import datetime

logging.basicConfig(
    filename='logs/firewall_activity.log', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s: %(message)s'
)

class FirewallLogger:
    def __init__(self, log_file='logs/firewall_activity.log'):
        pass

    def log_info(self, message):
        logging.info(message)

    def log_error(self, message):
        logging.error(message)

    def log_security_event(self, packet_info):
        # Specialized security logging
        pass
