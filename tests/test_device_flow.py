import pytest
from abstract_open_traffic_generator.config import Config
from abstract_open_traffic_generator.flow import *
from abstract_open_traffic_generator.flow_ipv4 import Priority, Dscp
from abstract_open_traffic_generator.port import *


def test_device_traffic():
    # ipv41 = Ipv4Device('West Ip', address='10.0.0.1', prefix=16, gateway='10.0.1.1')
    # eth1 = EthernetDevice('West Eth', children=[ipv41], mac='000000000001')
    # dev1 = Device('East Devices', sessions_per_port=1, protocols=[eth1])
    # ipv42 = Ipv4Device('East Ip', address='10.0.1.1', prefix=16, gateway='10.0.0.1')
    # eth2 = EthernetDevice('East Eth', children=[ipv42], mac='000000000002')
    # ethernet = Ethernet()
    # device = Device(name='Device1', parent=None, sessions_per_port=10, 
    #     protocols=[ethernet, vlan, ipv4])
    # tx = Port(name='Tx Port', location='1.1.1.1/1/1')
    # rx = Port(name='Rx Port', location='1.1.1.1/1/2')
    # device_group = DeviceGroup(name='DeviceGroup1', ports=[tx], 
    #     devices=[device])
    pass


if __name__ == '__main__':
    pytest.main(['-s', __file__])
