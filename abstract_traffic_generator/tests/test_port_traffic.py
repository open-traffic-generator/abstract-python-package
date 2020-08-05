import unittest
import json
from abstract_traffic_generator import *


class TestPortTraffic(unittest.TestCase):
    def test_port_eth_vlan_ipv4_traffic(self):
        tx = Port(name='Tx Port', location='1.1.1.1/1/1')
        rx = Port(name='Rx Port', location='1.1.1.1/1/2')
        flow = Flow(name='Tx -> Rx', endpoint=PortEndpoint(tx=tx.name),
            packet=[Ethernet(), Vlan(), Ipv4()])
        config = Config(ports=[tx, rx], flows=[flow])
        print(json.dumps(config, indent=2, default=lambda x: x.__dict__))
        assert(len(config.ports) == 2)
        assert(len(config.flows) == 1)

    def test_port_pfc_traffic(self):
        tx = Port(name='Tx', location='1.1.1.1/1/1')
        flow = Flow(name='Pfc Traffic', endpoint=PortEndpoint(tx=tx.name),
            packet=[PfcPause()])
        config = Config(ports=[tx], flows=[flow])
        print(json.dumps(config, indent=2, default=lambda x: x.__dict__))
        assert(len(config.ports) == 1)
        assert(len(config.flows) == 1)
        assert(config.flows[0].packet[0].type == 'PFCPAUSE')


if __name__ == '__main__':
    unittest.main()
