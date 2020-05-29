import pytest

from fixtures import DeviceFactory2DB, DeviceCategoryFactory2DB, EventAFactory2DB, EventBFactory2DB


@pytest.fixture
def create_device_category():
    return DeviceCategoryFactory2DB(name="Inclinometer", data_type="event_a")


@pytest.fixture
def create_device():
    return DeviceFactory2DB(name="ABC-1001", category="Inclinometer")


@pytest.mark.parametrize("test_input, test_output", [
    (["ABC-1001", "0.1", "2020-03-19T12:00:00+00:00"],
     ["0, ABC-1001, 0.1, 2020-03-19T12:00:00+00:00"])
])
def test_event_a_to_string(api_client, orm_client, create_device_category, create_device,
                           test_input, test_output):
    event = EventAFactory2DB(device_name=test_input[0],
                             value=test_input[1],
                             datetime=test_input[2])

    assert event.__str__() == test_output[0]


@pytest.mark.parametrize("test_input, test_output", [
    (["ABC-1001", 0.1, "2020-03-19T12:00:00+00:00"],
     ["0, ABC-1001, 0.1, 2020-03-19T12:00:00+00:00"])
])
def test_event_b_to_string(api_client, orm_client, create_device_category, create_device,
                           test_input, test_output):
    event = EventBFactory2DB(device_name=test_input[0],
                             value=test_input[1],
                             datetime=test_input[2])

    assert event.__str__() == test_output[0]


@pytest.mark.parametrize("test_input, test_output", [
    (["ABC-1001", "0.1", "2020-03-19T12:00:00+02:00"],
     ["0, ABC-1001, 0.1, 2020-03-19T10:00:00+00:00"])
])
def test_event_a_datetime_to_string(api_client, orm_client, create_device_category, create_device,
                                    test_input, test_output):
    event = EventAFactory2DB(device_name=test_input[0],
                             value=test_input[1],
                             datetime=test_input[2])

    assert event.__str__() == test_output[0]
