#!/usr/bin/env python3
import sys
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel


class SimpleTree(Topo):
    def build(self, n=2):
        dpid = 1
        core = self.addSwitch('c1', dpid='%x' % dpid)
        host_id = 1
        edge_id = 1
        for a in range(1, n + 1):
            dpid += 1
            agg = self.addSwitch('a%d' % a, dpid='%x' % dpid)
            self.addLink(core, agg)
            for _ in range(n):
                dpid += 1
                edge = self.addSwitch('e%d' % edge_id, dpid='%x' % dpid)
                edge_id += 1
                self.addLink(agg, edge)
                for _ in range(n):
                    host = self.addHost('h%d' % host_id)
                    host_id += 1
                    self.addLink(edge, host)


def run(n):
    net = Mininet(topo=SimpleTree(n), switch=OVSSwitch)
    net.start()
    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    n = int(sys.argv[1]) if len(sys.argv) > 1 else int(input('n = '))
    run(n)
