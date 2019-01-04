import pytest
import unittest
from gardena.sensor import Sensor
from tests.base_test_device import BaseTestDevice
from tests.gardena_api_return.devices_return import device_sensor_return


class SensorTestCase(unittest.TestCase, BaseTestDevice):
    def test_init(self):
        sensor = Sensor(smart_system=device_sensor_return)
        assert sensor.smart_system == device_sensor_return

    def test_init_exception_without_smart_system(self):
        with pytest.raises(ValueError):
            Sensor()

    def test_sensor_information(self):
        sensor = Sensor(smart_system=device_sensor_return)
        sensor.update_information(information=device_sensor_return)
        assert sensor.id == device_sensor_return["id"]
        assert sensor.name == device_sensor_return["name"]
        # XXX : no description for sensor ?
        # assert sensor.description == device_sensor_return["description"]
        assert sensor.category == device_sensor_return["category"]
        assert (
            sensor.is_configuration_synchronized
            == device_sensor_return["configuration_synchronized"]
        )
        assert sensor.serial_number == "12345678"
        assert sensor.version == "1.0.3-2.5.2-1.2.5-ICD1.17_1.0.18"
        assert sensor.last_time_online == "2019-01-03T23:57:34.549Z"
        assert sensor.device_state == "ok"
        assert sensor.battery_level == 97
        assert sensor.battery_status == "ok"
        assert sensor.radio_quality == 90
        assert sensor.radio_connection_status == "unknown"
        assert sensor.radio_state == "good"
        assert sensor.ambient_temperature == 22
        assert sensor.frost_warning == "no_frost"
        assert sensor.sensor_soil_temperature == 22
        assert sensor.sensor_soil_humidity == 0
        assert sensor.sensor_light == 0
        assert sensor.firmware_status == "up_to_date"
