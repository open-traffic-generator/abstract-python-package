import pytest


@pytest.fixture()
def serializer(request):
    class Serializer(object):
        def __init__(self, request):
            self.request = request
            self.test_name = getattr(request.node, "name")

        def json(self, obj):
            import json
            json_str = json.dumps(obj, indent=2, default=lambda x: x.__dict__)
            return '\n[%s] %s: %s\n' % (self.test_name, obj.__class__.__name__, json_str)
        
        def yaml(self, obj):
            import yaml
            yaml_str = yaml.dump(obj, indent=2)
            return '\n[%s] %s: %s\n' % (self.test_name, obj.__class__.__name__, yaml_str)

    return Serializer(request)            


@pytest.fixture(scope='module')
def tx():
    from abstract_open_traffic_generator.port import Port
    return Port(name='Tx', location='127.0.0.1;1;1')


@pytest.fixture(scope='module')
def rx():
    from abstract_open_traffic_generator.port import Port
    return Port(name='Rx', location='127.0.0.1;1;2')


@pytest.fixture(scope='module')
def port_ipv4_traffic(tx):
    from abstract_open_traffic_generator.flow import Flow, Pattern, Ipv4
    from abstract_open_traffic_generator.flow import Ethernet, Vlan, Header, Endpoint, PortEndpoint
    from abstract_open_traffic_generator.flow import Size, Rate
    eth = Ethernet(dst=Pattern('00:00:01:00:00:01'), 
        src=Pattern('00:00:02:00:00:01'))
    vlan = Vlan(priority=Pattern(['0', '1', '2']), 
        cfi=Pattern('0'), 
        id=Pattern('1'))
    ipv4 = Ipv4(src=Pattern('1.1.1.1'), 
        dst=Pattern('1.1.2.1'))
    return Flow(name='Port Based Ipv4 Traffic', 
        endpoint=Endpoint(PortEndpoint(tx_port_name=tx.name)),
        packet=[Header(eth), Header(vlan), Header(ipv4)],
        size=Size(512),
        rate=Rate(unit='pps', value=1000000))
