import pytest
from abstract_open_traffic_generator.state import Config
from abstract_open_traffic_generator.flow import *
from abstract_open_traffic_generator.flow_ipv4 import Priority, Dscp
from abstract_open_traffic_generator.port import *


def test_port_traffic(serializer):
    location = Location(Physical(address='127.0.0.1', board=1, port=1))
    tx = Port(name='Tx', location=location)
    ipv4 = Ipv4(src=StringPattern('1.1.1.1'), 
        dst=StringPattern(StringCounter(start='1.1.2.1', step='0.0.0.1', direction='increment', count=10)), 
        priority=Priority(Dscp(phb=NumberPattern(Dscp.PHB_EF46), ecn=NumberPattern(Dscp.ECN_CAPABLE_TRANSPORT_1))))
    background = Flow(name='Background Traffic', 
        endpoint=Endpoint(PortEndpoint(tx_port=tx.name)),
        packet=[Header(Ethernet()), Header(Vlan()), Header(ipv4)],
        size=Size(512),
        rate=Rate(unit='pps', value=1000000))
    pfc = Flow(name='Pfc Traffic', 
        endpoint=Endpoint(PortEndpoint(tx_port=tx.name)),
        packet=[Header(PfcPause())],
        size=Size(64),
        rate=Rate(unit='pps', value=1000000))
    config = Config(state='CREATE', ports=[tx], flows=[background, pfc])
    print(serializer.json(config))


if __name__ == '__main__':
    pytest.main(['-s', __file__])
