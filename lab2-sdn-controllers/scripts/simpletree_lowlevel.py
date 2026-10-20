#!/usr/bin/env python3
import sys
from mininet.net import Mininet
from mininet.node import OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel


def build(n):
    net = Mininet(switch=OVSSwitch)
    net.addController('c0')
    dpid = 1
    core = net.addSwitch('c1', dpid='%x' % dpid)
    host_id = 1
    edge_id = 1
    for a in range(1, n + 1):
        dpid += 1
        agg = net.addSwitch('a%d' % a, dpid='%x' % dpid)
        net.addLink(core, agg)
        for _ in range(n):
            dpid += 1
            edge = net.addSwitch('e%d' % edge_id, dpid='%x' % dpid)
            edge_id += 1
            net.addLink(agg, edge)
            for _ in range(n):
                host = net.addHost('h%d' % host_id)
                host_id += 1
                net.addLink(edge, host)
    return net


if __name__ == '__main__':
    setLogLevel('info')
    n = int(sys.argv[1]) if len(sys.argv) > 1 else int(input('n = '))
    net = build(n)
    net.start()
    CLI(net)
    net.stop()
