import json

import pytest

from fixtures import DeviceFactory2DB, DeviceCategoryFactory2DB, EventAFactory2DB, \
    EventBFactory2DB, EventADictFactory
from models.models import Event
from translators import model_translators


def assert_events(event_api, event_db):
    # assert event_db["id"] == event_api["id"]
    assert event_db["device_name"] == event_api["device_name"]
    assert event_db["value"] == event_api["value"]
    if isinstance(event_db["datetime"], str):
        assert event_db["datetime"] == event_api["datetime"]
    else:
        assert model_translators.translate_datetime(event_db["datetime"]) == event_api["datetime"]


@pytest.fixture
def create_device_category():
    return DeviceCategoryFactory2DB(name="Inclinometer", data_type="event_a")


@pytest.fixture
def create_device():
    return DeviceFactory2DB(name="a")


@pytest.mark.parametrize("test_input, test_input_2", [
    (["a", "0.1", "2020-03-18T12:00:00+00:00"],
     ["a", "0.2", "2020-03-18T12:02:00+00:00"])
])
def test_get_events_all(api_client, orm_client, create_device_category, create_device,
                         test_input, test_input_2):
    assert orm_client.session.query(Event).count() == 0
    event_1 = EventAFactory2DB(device_name=test_input[0],
                               value=test_input[1],
                               datetime=test_input[2])
    assert orm_client.session.query(Event).count() == 1
    event_2 = EventBFactory2DB(device_name=test_input_2[0],
                               value=test_input_2[1],
                               datetime=test_input_2[2])
    assert orm_client.session.query(Event).count() == 2

    rv = api_client.get(f"/events/")
    assert rv.status_code == 200
    response_content_1 = json.loads(rv.data)['data'][0]
    response_content_2 = json.loads(rv.data)['data'][1]
    assert_events(response_content_1, event_1.__dict__)
    assert_events(response_content_2, event_2.__dict__)


@pytest.mark.parametrize("test_input", [
    (["a", "0.1", "2020-03-18T12:00:00+00:00"])
])
def test_get_event_a(api_client, orm_client, create_device_category, create_device,
                     test_input):
    assert orm_client.session.query(Event).count() == 0
    event_1 = EventAFactory2DB(device_name=test_input[0],
                               value=test_input[1],
                               datetime=test_input[2])
    assert orm_client.session.query(Event).count() == 1

    rv = api_client.get(f"/events/{event_1.id}")
    assert rv.status_code == 200
    response_content = json.loads(rv.data)['data']
    assert_events(response_content, event_1.__dict__)


@pytest.mark.parametrize("test_input", [
    (["a", "0.1", "2020-03-18T12:00:00+00:00"])
])
def test_get_event_b(api_client, orm_client, create_device_category, create_device,
                     test_input):
    assert orm_client.session.query(Event).count() == 0
    event_1 = EventBFactory2DB(device_name=test_input[0],
                               value=test_input[1],
                               datetime=test_input[2])
    assert orm_client.session.query(Event).count() == 1

    rv = api_client.get(f"/events/{event_1.id}")
    assert rv.status_code == 200
    response_content = json.loads(rv.data)['data']
    assert_events(response_content, event_1.__dict__)


@pytest.mark.parametrize("test_input", [
    (["a", "0.1", "2020-03-18T12:00:00+00:00"])
])
def test_add_event(api_client, orm_client, create_device_category, create_device,
                   test_input):
    assert orm_client.session.query(Event).count() == 0
    event_1 = EventADictFactory(device_name=test_input[0],
                                value=test_input[1],
                                datetime=test_input[2])
    assert orm_client.session.query(Event).count() == 0

    rv = api_client.post("/events/", json=event_1)
    assert rv.status_code == 200, rv.data
    response_content = json.loads(rv.data)['data']['id']

    # TODO Change to orm_client.session.query...
    rv = api_client.get(f"/events/{response_content}")
    assert rv.status_code == 200
    response_content = json.loads(rv.data)['data']
    assert_events(response_content, event_1)


@pytest.mark.parametrize("test_input", [
    (["a", "0.1", "2020-03-18T12:00:00+00:00"])
])
def test_delete_event(api_client, orm_client, create_device_category, create_device,
                      test_input):
    assert orm_client.session.query(Event).count() == 0
    event_1 = EventAFactory2DB(device_name=test_input[0],
                               value=test_input[1],
                               datetime=test_input[2])
    assert orm_client.session.query(Event).count() == 1

    rv = api_client.delete(f"/events/{event_1.id}")
    assert rv.status_code == 200

    assert orm_client.session.query(Event).count() == 0
