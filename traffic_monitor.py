from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.recoco import Timer
from pox.lib.packet.ipv4 import ipv4

log = core.getLogger()

# Dictionary to store traffic stats
traffic_stats = {}

def _handle_PacketIn(event):
    packet = event.parsed

    if not packet.parsed:
        return

    ip_packet = packet.find('ipv4')

    if ip_packet:
        src = ip_packet.srcip
        dst = ip_packet.dstip
        key = (src, dst)

        length = len(packet)

        if key not in traffic_stats:
            traffic_stats[key] = {"packets":0, "bytes":0}

        traffic_stats[key]["packets"] += 1
        traffic_stats[key]["bytes"] += length


def print_stats():
    print("\n================ TRAFFIC STATISTICS ================")
    print("SRC IP\t\tDST IP\t\tPACKETS\t\tBYTES")

    for (src, dst), stats in traffic_stats.items():
        print(f"{src}\t{dst}\t{stats['packets']}\t\t{stats['bytes']}")

    print("====================================================\n")


def launch():

    log.info("Traffic Monitoring Module Loaded")

    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)

    # Print stats every 5 seconds
    Timer(5, print_stats, recurring=True)
