from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpidToStr
from pox.lib.recoco import Timer

log = core.getLogger()

class TrafficMonitor(object):

    def __init__(self):
        core.openflow.addListeners(self)
        Timer(10, self.request_stats, recurring=True)

    def _handle_ConnectionUp(self, event):
        log.info("Switch %s connected", dpidToStr(event.dpid))

    def request_stats(self):
        for connection in core.openflow._connections.values():
            connection.send(of.ofp_stats_request(body=of.ofp_flow_stats_request()))

    def _handle_FlowStatsReceived(self, event):

        log.info("Flow stats from switch %s", dpidToStr(event.connection.dpid))

        for stat in event.stats:
            log.info("Match: %s  Packets: %s  Bytes: %s",
                     stat.match,
                     stat.packet_count,
                     stat.byte_count)

def launch():
    core.registerNew(TrafficMonitor)
