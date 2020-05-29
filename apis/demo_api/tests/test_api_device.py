import json

import pytest

from fixtures import DeviceFactory2DB, DeviceDictFactory, DeviceCategoryFactory2DB, \
    LocationFactory2DB
from models.models import Device


@pytest.fixture
def create_device_category():
    return DeviceCategoryFactory2DB(name="Inclinometer", data_type="event_a")


@pytest.fixture
def create_location():
    return LocationFactory2DB(name="MyLocation1")


def assert_devices(device_api, device_db):
    # assert device_db["id"] == device_api["id"]
    assert device_db["name"] == device_api["name"]
    assert device_db["category"] == device_api["category"]
    assert device_db["location"] == device_api["location"]


@pytest.mark.parametrize("test_input, test_input_2", [
    (["a", "Inclinometer", "MyLocation1"],
     ["b", "Inclinometer", "MyLocation1"])
])
def test_get_devices_all(api_client, orm_client, create_device_category, create_location,
                         test_input, test_input_2):
    assert orm_client.session.query(Device).count() == 0
    device_1 = DeviceFactory2DB(name=test_input[0],
                                category=test_input[1],
                                location=test_input[2])
    assert orm_client.session.query(Device).count() == 1
    device_2 = DeviceFactory2DB(name=test_input_2[0],
                                category=test_input_2[1],
                                location=test_input_2[2])
    assert orm_client.session.query(Device).count() == 2

    rv = api_client.get(f"/devices/")
    assert rv.status_code == 200
    response_content_1 = json.loads(rv.data)['data'][0]
    response_content_2 = json.loads(rv.data)['data'][1]
    assert_devices(response_content_1, device_1.__dict__)
    assert_devices(response_content_2, device_2.__dict__)


@pytest.mark.parametrize("test_input", [
    (["a", "Inclinometer", "MyLocation1"])
])
def test_get_device(api_client, orm_client, create_device_category, create_location,
                    test_input):
    assert orm_client.session.query(Device).count() == 0
    device_1 = DeviceFactory2DB(name=test_input[0],
                                category=test_input[1],
                                location=test_input[2])
    assert orm_client.session.query(Device).count() == 1

    rv = api_client.get(f"/devices/{device_1.name}")
    assert rv.status_code == 200
    response_content = json.loads(rv.data)['data']
    assert_devices(response_content, device_1.__dict__)


@pytest.mark.parametrize("test_input", [
    (["a", "Inclinometer", "MyLocation1"]),
    (["a", "Inclinometer", None])
])
def test_add_device(api_client, orm_client, create_device_category, create_location,
                    test_input):
    assert orm_client.session.query(Device).count() == 0
    device_1 = DeviceDictFactory(name=test_input[0],
                                 category=test_input[1],
                                 location=test_input[2])
    assert orm_client.session.query(Device).count() == 0

    rv = api_client.post("/devices/", json=device_1)
    assert rv.status_code == 200, rv.data
    response_content = json.loads(rv.data)['data']['name']
    assert response_content == device_1["name"]

    # TODO Change to orm_client.session.query...
    rv = api_client.get(f"/devices/{response_content}")
    assert rv.status_code == 200
    response_content = json.loads(rv.data)['data']
    assert_devices(response_content, device_1)


@pytest.mark.parametrize("test_input, test_modify", [
    (["a", "Inclinometer", "MyLocation1"],
     ["a", "Inclinometer", "MyLocation1"])
])
def test_update_device(api_client, orm_client, create_device_category, create_location,
                       test_input, test_modify):
    assert orm_client.session.query(Device).count() == 0
    device_1 = DeviceFactory2DB(name=test_input[0],
                                category=test_input[1],
                                location=test_input[2])
    assert orm_client.session.query(Device).count() == 1

    device_to_modify = DeviceDictFactory(name=test_input[0],
                                         category=test_input[1],
                                         location=test_input[2])

    rv = api_client.put(f"/devices/{device_1.name}",
                        json=device_to_modify)
    assert rv.status_code == 200
    assert orm_client.session.query(Device).count() == 1

    rv = api_client.get(f"/devices/{device_1.name}")
    assert rv.status_code == 200
    response_content = json.loads(rv.data)['data']
    assert_devices(response_content, device_to_modify)


@pytest.mark.parametrize("test_input", [
    (["a", "Inclinometer", "MyLocation1"])
])
def test_delete_device(api_client, orm_client, create_device_category, create_location,
                       test_input):
    assert orm_client.session.query(Device).count() == 0
    device_1 = DeviceFactory2DB(name=test_input[0],
                                category=test_input[1],
                                location=test_input[2])
    assert orm_client.session.query(Device).count() == 1

    rv = api_client.delete(f"/devices/{device_1.name}")
    assert rv.status_code == 200

    assert orm_client.session.query(Device).count() == 0
