import pytest
from abstract_open_traffic_generator.state import Config


def test_config_create(serializer, tx, rx, port_ipv4_traffic):
    config = Config(state='CREATE', ports=[tx], flows=[port_ipv4_traffic])
    print(serializer.json(config))


# def test_config_update(serializer, tx, rx, device_traffic):
#     config = Config(state='UPDATE', ports=[tx, rx], flows=[device_traffic])
#     print(serializer.json(config))


if __name__ == '__main__':
    pytest.main(['-s', __file__])
