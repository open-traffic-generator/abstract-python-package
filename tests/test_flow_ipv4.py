import pytest
from abstract_open_traffic_generator.flow import *
from abstract_open_traffic_generator.flow_ipv4 import Priority, Dscp


def test_ipv4_priority_dscp(serializer):
    dscp = Dscp(phb=NumberPattern(Dscp.PHB_CS6))
    dscp_priority = Priority(dscp)
    print(serializer.yaml(dscp_priority))


def test_ipv4_priority_dscp_ecn(serializer):
    dscp = Dscp(phb=NumberPattern(Dscp.PHB_CS7), 
        ecn=NumberPattern(Dscp.ECN_CAPABLE_TRANSPORT_1))
    dscp_priority = Priority(dscp)
    print(serializer.yaml(dscp_priority))


def test_ipv4_priority_raw(serializer):
    counter = NumberCounter(start=1, step=1, direction='increment', count=4)
    pattern = NumberPattern(counter)
    raw_priority = Priority(pattern)
    print(serializer.yaml(raw_priority))


def test_ipv4(serializer):
    src = StringPattern(StringCounter(start='1.1.1.1', step='0.0.0.1', direction='increment', count=10))
    dst = StringPattern(StringCounter(start='1.1.2.1', step='0.0.0.1', direction='increment', count=10))
    ipv4 = Ipv4(src=src, dst=dst, priority=Priority(NumberPattern(1)))
    print(serializer.yaml(ipv4))


if __name__ == '__main__':
    pytest.main(['-s', __file__])
