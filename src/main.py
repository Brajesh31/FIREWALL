import os
import logging

class FirewallLogger:
    def __init__(self):
        log_file = 'D:/PROJECTS/FIREWALL/src/logs/firewall_activity.log'
        log_dir = os.path.dirname(log_file)
        
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Create a console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

        # Add the console handler to the root logger
        logging.getLogger().addHandler(console_handler)

    def log_info(self, message):
        logging.info(message)

    def log_error(self, message):
        logging.error(message)