import pytest
from abstract_open_traffic_generator.config import Config
from abstract_open_traffic_generator.port import Port
from abstract_open_traffic_generator.device import *


def test_devices(serializer):
    """Demonstrate how to build a device configuration on a port
    """
    config = Config()
    config.ports.append(Port(name='port1'))
    bgpv4 = Bgpv4(name='bgpv4',
                  ipv4=Ipv4(name='ipv4',
                            ethernet=Ethernet(name='eth1',
                                              vlans=[
                                                  Vlan(name='vlan1'),
                                                  Vlan(name='vlan2'),
                                                  Vlan(name='vlan3')
                                              ])))
    device = Device(name='device',
                    container_name=config.ports[0].name,
                    choice=bgpv4,
                    device_count=10)
    config.devices.append(device)
    print(serializer.json(config))


if __name__ == '__main__':
    pytest.main(['-s', __file__])
