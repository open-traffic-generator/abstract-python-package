import pytest
from abstract_open_traffic_generator.config import Config
from abstract_open_traffic_generator.device import *


def test_devices(serializer):
    bgpv4 = Bgpv4(name='bgpv4')
    ipv4 = Ipv4(name='ipv4',
                bgpv4=bgpv4)
    ipv61 = Ipv6(name='ipv6')
    vlan1 = Vlan(name='vlan1')
    vlan2 = Vlan(name='vlan2')
    vlan3 = Vlan(name='vlan3')
    eth1 = Ethernet(name='eth1',
                    vlans=[vlan1, vlan2, vlan3],
                    ipv4=ipv4,
                    ipv6=ipv61)
    ipv62 = Ipv6(name='ipv62')
    eth2 = Ethernet(name='eth2', ipv6=ipv62)
    eth3 = Ethernet(name='eth3')
    device1 = Device(name='device1',
                     devices_per_port=1,
                     ethernets=[eth3])
    device2 = Device(name='device2',
                     devices_per_port=1,
                     devices=[device1],
                     ethernets=[eth1, eth2])
    device_group = DeviceGroup(name='devicegroup',
                               devices=[device2])
    config = Config(
        device_groups=[device_group]
    )
    print(serializer.json(config))


if __name__ == '__main__':
    pytest.main(['-s', __file__])
