import pytest
from abstract_open_traffic_generator.flow import *
from abstract_open_traffic_generator.flow_ipv4 import Priority, Dscp


def test_ipv4_fixed_priority_dscp(serializer):
    dscp = Dscp(phb=Pattern(Dscp.PHB_CS6))
    dscp_priority = Priority(dscp)
    print(serializer.json(dscp_priority))


def test_ipv4_list_priority_dscp(serializer):
    phb_list = [
        Dscp.PHB_AF11,
        Dscp.PHB_AF21,
        Dscp.PHB_AF43,
        Dscp.PHB_CS3,
        Dscp.PHB_CS7
    ]
    dscp = Dscp(phb=Pattern(phb_list))
    dscp_priority = Priority(dscp)
    print(serializer.json(dscp_priority))


def test_ipv4_counter_priority_dscp(serializer):
    phb_counter = Counter(start='10', step='1', count=6, up=True)
    dscp = Dscp(phb=Pattern(phb_counter))
    dscp_priority = Priority(dscp)
    print(serializer.json(dscp_priority))


def test_ipv4_priority_dscp_ecn(serializer):
    dscp = Dscp(phb=Pattern(Dscp.PHB_CS7), 
        ecn=Pattern(Dscp.ECN_CAPABLE_TRANSPORT_1))
    dscp_priority = Priority(dscp)
    print(serializer.json(dscp_priority))


def test_ipv4_priority_raw(serializer):
    counter = Counter(start='1', step='1', count=4, up=True)
    pattern = Pattern(counter)
    raw_priority = Priority(pattern)
    print(serializer.json(raw_priority))


def test_ipv4(serializer):
    ipv4 = Ipv4(src= Pattern(Counter(start='1.1.1.1', step='0.0.0.1', count=10)), 
        dst=Pattern(Counter(start='1.1.2.1', step='0.0.0.1', count=10)), 
        priority=Priority(Pattern(Priority.PRIORITY_RAW)))
    print(serializer.json(ipv4))


if __name__ == '__main__':
    pytest.main(['-s', __file__])
