import pytest
from abstract_open_traffic_generator.config import Config
from abstract_open_traffic_generator.flow import *
from abstract_open_traffic_generator.flow_ipv4 import Priority, Dscp


def test_port_traffic(serializer, tx, rx):
    dscp = Dscp(phb=Pattern(Dscp.PHB_EF46), 
        ecn=Pattern(Dscp.ECN_CAPABLE_TRANSPORT_1))
    ipv4 = Ipv4(src=Pattern('1.1.1.1'), 
        dst=Pattern(Counter(start='1.1.2.1', step='0.0.0.1', count=10)), 
        priority=Priority(dscp))
    background = Flow(name='Background Traffic', 
        endpoint=Endpoint(PortEndpoint(tx_port_name=tx.name)),
        packet=[Header(Ethernet()), Header(Vlan()), Header(ipv4)],
        size=Size(512),
        rate=Rate(unit='pps', value=1000000),
        duration=Duration(Fixed(packets=0)))
    config = Config(ports=[tx], flows=[background])
    print(serializer.json(config))


def test_port_pfc_pause_traffic(serializer, tx, rx):
    pfc_pause = PfcPause(dst=Pattern('000001020304'),
        src=Pattern('0000002030405'),
        control_op_code=Pattern('01'))
    pfc_flow = Flow(name='Pfc Traffic', 
        endpoint=Endpoint(PortEndpoint(tx_port_name=tx.name)),
        packet=[Header(pfc_pause)],
        size=Size(64),
        rate=Rate(unit='pps', value=1000000),
        duration=Duration(Burst(packets=10000)))
    config = Config(ports=[tx], flows=[pfc_flow])
    print(serializer.json(config))


if __name__ == '__main__':
    pytest.main(['-s', __file__])
