import threading
import scapy.all as scapy

class NetworkMonitor:
    def __init__(self, packet_inspector):
        self.packet_inspector = packet_inspector
        self.monitoring_thread = None

    def start_monitoring(self):
        self.monitoring_thread = threading.Thread(
            target=self.capture_packets, 
            daemon=True
        )
        self.monitoring_thread.start()

    def capture_packets(self):
        scapy.sniff(
            prn=self.packet_inspector.inspect_packet, 
            store=0
        )
