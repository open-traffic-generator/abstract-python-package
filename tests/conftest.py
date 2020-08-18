import pytest


@pytest.fixture()
def serializer(request):
    class Serializer(object):
        def __init__(self, request):
            self.request = request

        def json(self, obj):
            import json
            json_str = json.dumps(obj, indent=2, default=lambda x: x.__dict__)
            test_name = getattr(request.node, "name")
            return '\n[%s] %s: %s\n' % (test_name, obj.__class__.__name__, json_str)
    return Serializer(request)            

@pytest.fixture(scope='module')
def b2b_ports():
    from abstract_open_traffic_generator.port import Port
    return [
        Port(name='Tx Port'),
        Port(name='Rx Port')
    ]
