import pytest


@pytest.fixture(scope='module')
def serializer():
    class Serializer(object):
        def json(self, obj):
            import json
            return json.dumps(obj, indent=2, default=lambda x: x.__dict__)
    return Serializer()            

@pytest.fixture(scope='module')
def b2b_ports():
    from abstract_open_traffic_generator.port import Port
    return [
        Port(name='Tx Port'),
        Port(name='Rx Port')
    ]

