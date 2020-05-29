import pytest

from fixtures import DeviceFactory2DB, DeviceCategoryFactory2DB, LocationFactory2DB


@pytest.fixture
def create_device_category():
    return DeviceCategoryFactory2DB(name="Inclinometer", data_type="event_a")


@pytest.fixture
def create_location():
    return LocationFactory2DB(name="MyLocation1")


@pytest.mark.parametrize("test_input, test_output", [
    (["a", "Inclinometer", "MyLocation1"],
     ["0, a, Inclinometer, MyLocation1"])
])
def test_device_to_string(api_client, orm_client, create_device_category, create_location,
                          test_input, test_output):
    device = DeviceFactory2DB(name=test_input[0],
                              category=test_input[1],
                              location=test_input[2])

    assert device.__str__() == test_output[0]


@pytest.mark.parametrize("test_input, test_output", [
    (["a", "Inclinometer"],
     ["0, a, Inclinometer, None"])
])
def test_device_no_location_to_string(api_client, orm_client, create_device_category,
                                      test_input, test_output):
    device = DeviceFactory2DB(name=test_input[0],
                              category=test_input[1])

    assert device.__str__() == test_output[0]
