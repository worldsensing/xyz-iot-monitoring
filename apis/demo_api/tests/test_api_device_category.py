import json

import pytest

from fixtures import DeviceCategoryFactory2DB, \
    DeviceCategoryDictFactory
from models.models import DeviceCategory


def assert_device_categories(device_category_api, device_category_db):
    # assert device_db["id"] == device_api["id"]
    assert device_category_db["name"] == device_category_api["name"]
    assert device_category_db["data_type"] == device_category_api["data_type"]


@pytest.mark.parametrize("test_input, test_input_2", [
    (["Inclinometer", "event_a"],
     ["Accelerometer", "event_b"])
])
def test_get_device_categories_all(api_client, orm_client,
                                   test_input, test_input_2):
    assert orm_client.session.query(DeviceCategory).count() == 0
    device_category_1 = DeviceCategoryFactory2DB(name=test_input[0],
                                                 data_type=test_input[1])
    assert orm_client.session.query(DeviceCategory).count() == 1
    device_category_2 = DeviceCategoryFactory2DB(name=test_input_2[0],
                                                 data_type=test_input_2[1])
    assert orm_client.session.query(DeviceCategory).count() == 2

    rv = api_client.get(f"/device-categories/")
    assert rv.status_code == 200
    response_content_1 = json.loads(rv.data)['data'][0]
    response_content_2 = json.loads(rv.data)['data'][1]
    assert_device_categories(response_content_1, device_category_1.__dict__)
    assert_device_categories(response_content_2, device_category_2.__dict__)


@pytest.mark.parametrize("test_input", [
    (["Inclinometer", "event_a"])
])
def test_get_device_category(api_client, orm_client,
                             test_input):
    assert orm_client.session.query(DeviceCategory).count() == 0
    device_category_1 = DeviceCategoryFactory2DB(name=test_input[0],
                                                 data_type=test_input[1])
    assert orm_client.session.query(DeviceCategory).count() == 1

    rv = api_client.get(f"/device-categories/{device_category_1.name}")
    assert rv.status_code == 200
    response_content = json.loads(rv.data)['data']
    assert_device_categories(response_content, device_category_1.__dict__)


@pytest.mark.parametrize("test_input", [
    (["Inclinometer", "event_a"])
])
def test_add_device_category(api_client, orm_client,
                             test_input):
    assert orm_client.session.query(DeviceCategory).count() == 0
    device_category_1 = DeviceCategoryDictFactory(name=test_input[0],
                                                  data_type=test_input[1])
    assert orm_client.session.query(DeviceCategory).count() == 0

    rv = api_client.post("/device-categories/", json=device_category_1)
    assert rv.status_code == 200, rv.data
    response_content = json.loads(rv.data)['data']['name']
    assert response_content == device_category_1["name"]

    # TODO Change to orm_client.session.query...
    rv = api_client.get(f"/device-categories/{response_content}")
    assert rv.status_code == 200
    response_content = json.loads(rv.data)['data']
    assert_device_categories(response_content, device_category_1)


@pytest.mark.parametrize("test_input, test_modify", [
    (["Inclinometer", "event_a"],
     ["Inclinometer", "event_b"])
])
def test_update_device(api_client, orm_client,
                       test_input, test_modify):
    assert orm_client.session.query(DeviceCategory).count() == 0
    device_category_1 = DeviceCategoryFactory2DB(name=test_input[0],
                                                 data_type=test_input[1])
    assert orm_client.session.query(DeviceCategory).count() == 1

    device_category_to_modify = DeviceCategoryDictFactory(name=test_modify[0],
                                                          data_type=test_modify[1])

    rv = api_client.put(f"/device-categories/{device_category_1.name}",
                        json=device_category_to_modify)
    assert rv.status_code == 200
    assert orm_client.session.query(DeviceCategory).count() == 1

    rv = api_client.get(f"/device-categories/{device_category_1.name}")
    assert rv.status_code == 200
    response_content = json.loads(rv.data)['data']
    assert_device_categories(response_content, device_category_to_modify)


@pytest.mark.parametrize("test_input", [
    (["Inclinometer", "event_a"])
])
def test_delete_device(api_client, orm_client,
                       test_input):
    assert orm_client.session.query(DeviceCategory).count() == 0
    device_category_1 = DeviceCategoryFactory2DB(name=test_input[0],
                                                 data_type=test_input[1])
    assert orm_client.session.query(DeviceCategory).count() == 1

    rv = api_client.delete(f"/device-categories/{device_category_1.name}")
    assert rv.status_code == 200

    assert orm_client.session.query(DeviceCategory).count() == 0
