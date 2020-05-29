import json

import pytest

from fixtures import DeviceFactory2DB, DeviceCategoryDictFactory, \
    DeviceDictFactory, EventADictFactory, EventAFactory2DB, DeviceCategoryFactory2DB, \
    LocationDictFactory, LocationFactory2DB
from models.models import Device, Event, DeviceCategory
from translators import model_translators


@pytest.fixture
def create_device_category():
    return DeviceCategoryFactory2DB()


@pytest.fixture
def create_location():
    return LocationFactory2DB(name="MyLocation1")


def assert_device_categories(device_category_api, device_category_db):
    # assert device_db["id"] == device_api["id"]
    assert device_category_db["name"] == device_category_api["name"]
    assert device_category_db["data_type"] == device_category_api["data_type"]


def assert_locations(location_api, location_db):
    # assert location_db["id"] == location_api["id"]
    assert location_db["name"] == location_api["name"]
    assert location_db["latlng"] == location_api["latlng"]


def assert_devices(device_api, device_db):
    # assert device_db["id"] == device_api["id"]
    assert device_db["name"] == device_api["name"]
    assert device_db["category"] == device_api["category"]
    assert device_db["location"] == device_api["location"]


def assert_events(event_api, event_db):
    # assert event_db["id"] == event_api["id"]
    assert event_db["device_name"] == event_api["device_name"]
    assert event_db["value"] == event_api["value"]
    if isinstance(event_db["datetime"], str):
        assert event_db["datetime"] == event_api["datetime"]
    else:
        assert model_translators.translate_datetime(event_db["datetime"]) == event_api["datetime"]


@pytest.mark.parametrize(
    "test_input_device_category, test_input_location, test_input_device, test_input_event", [
        (["Inclinometer", "event_a"],
         ["MyLocation1", "41.2, 2.1"],
         ["device_a", "Inclinometer", "MyLocation1"],
         ["device_a", "0.1", "2020-03-19T12:00:00+00:00"])
    ])
def test_full_api(api_client, orm_client,
                  test_input_device_category, test_input_location, test_input_device,
                  test_input_event):
    # Device category checks
    ## Create device_category element
    device_category = DeviceCategoryDictFactory(name=test_input_device_category[0],
                                                data_type=test_input_device_category[1])
    rv = api_client.post("/device-categories/", json=device_category)
    assert rv.status_code == 200, rv.data
    response_content = json.loads(rv.data)['data']['name']
    assert response_content == device_category["name"]

    ## Check device_category creation
    rv = api_client.get(f"/device-categories/{response_content}")
    assert rv.status_code == 200
    response_content = json.loads(rv.data)['data']
    assert_device_categories(response_content, device_category)

    ## Create location element
    location = LocationDictFactory(name=test_input_location[0],
                                   latlng=test_input_location[1])
    rv = api_client.post("/locations/", json=location)
    assert rv.status_code == 200, rv.data
    response_content = json.loads(rv.data)['data']['name']
    assert response_content == location["name"]

    ## Check location creation
    rv = api_client.get(f"/locations/{response_content}")
    assert rv.status_code == 200
    response_content = json.loads(rv.data)['data']
    assert_locations(response_content, location)

    # Device checks
    ## Create the device element
    device = DeviceDictFactory(name=test_input_device[0],
                               category=test_input_device[1],
                               location=test_input_device[2])

    rv = api_client.post("/devices/", json=device)
    assert rv.status_code == 200, rv.data
    response_content = json.loads(rv.data)['data']['name']
    assert response_content == device["name"]

    ## Check device creation
    rv = api_client.get(f"/devices/{response_content}")
    assert rv.status_code == 200
    response_content = json.loads(rv.data)['data']
    assert_devices(response_content, device)

    # EventA checks
    ## Create the event element
    event_a = EventADictFactory(device_name=test_input_event[0],
                                value=test_input_event[1],
                                datetime=test_input_event[2])
    rv = api_client.post("/events/", json=event_a)
    assert rv.status_code == 200, rv.data
    response_content = json.loads(rv.data)['data']['id']

    ## Check event creation
    rv = api_client.get(f"/events/{response_content}")
    assert rv.status_code == 200
    response_content = json.loads(rv.data)['data']
    assert_events(response_content, event_a)


@pytest.mark.parametrize("test_input", [
    (["device_a", "Inclinometer", "MyLocation1"])
])
def test_delete_device_with_events(api_client, orm_client, create_device_category, create_location,
                                   test_input):
    assert orm_client.session.query(Device).count() == 0
    device = DeviceFactory2DB(name=test_input[0],
                              category=test_input[1],
                              location=test_input[2])
    assert orm_client.session.query(Device).count() == 1

    assert orm_client.session.query(Event).count() == 0
    EventAFactory2DB(device_name=test_input[0])
    assert orm_client.session.query(Event).count() == 1

    rv = api_client.delete(f"/devices/{device.name}")
    assert rv.status_code == 200

    assert orm_client.session.query(Device).count() == 0
    assert orm_client.session.query(Event).count() == 0


@pytest.mark.parametrize("test_device_category, test_device, test_event", [
    (["Inclinometer", "event_a"],
     ["device_a", "Inclinometer", "MyLocation1"],
     ["device_a", "0.1", "2020-03-18T12:00:00+00:00"])
])
def test_insert_event_category_deleted(api_client, orm_client, create_location,
                                       test_device_category, test_device, test_event):
    assert orm_client.session.query(DeviceCategory).count() == 0
    device_category = DeviceCategoryFactory2DB(name=test_device_category[0],
                                               data_type=test_device_category[1])
    assert orm_client.session.query(DeviceCategory).count() == 1

    assert orm_client.session.query(Device).count() == 0
    device = DeviceFactory2DB(name=test_device[0],
                              category=test_device[1],
                              location=test_device[2])
    assert orm_client.session.query(Device).count() == 1

    assert orm_client.session.query(Event).count() == 0
    EventAFactory2DB(device_name=test_device[0])
    assert orm_client.session.query(Event).count() == 1

    # Delete a device category. Not possible because the Device has its category
    rv = api_client.delete(f"/device-categories/{device_category.name}")
    assert rv.status_code == 400
    assert orm_client.session.query(DeviceCategory).count() == 1
    assert orm_client.session.query(Device).count() == 1
    assert orm_client.session.query(Event).count() == 1

    # Device is deleted. Also its events
    rv = api_client.delete(f"/devices/{device.name}")
    assert rv.status_code == 200
    assert orm_client.session.query(DeviceCategory).count() == 1
    assert orm_client.session.query(Device).count() == 0
    assert orm_client.session.query(Event).count() == 0

    # Insert a new event, but its device has no category
    EventADictFactory(device_name=test_event[0],
                      value=test_event[1],
                      datetime=test_event[2])

    # Delete a device category without any device
    rv = api_client.delete(f"/device-categories/{device_category.name}")
    assert rv.status_code == 200
    assert orm_client.session.query(DeviceCategory).count() == 0
    assert orm_client.session.query(Device).count() == 0
    assert orm_client.session.query(Event).count() == 0
