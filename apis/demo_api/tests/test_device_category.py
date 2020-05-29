import pytest

from fixtures import DeviceCategoryFactory2DB


@pytest.mark.parametrize("test_input, test_output", [
    (["Inclinometer", "event_a"],
     ["0, Inclinometer, event_a"])
])
def test_device_category_to_string(api_client, orm_client,
                                   test_input, test_output):
    device_category = DeviceCategoryFactory2DB(name=test_input[0],
                                               data_type=test_input[1])

    assert device_category.__str__() == test_output[0]
