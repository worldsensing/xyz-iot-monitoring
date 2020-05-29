import pytest

from fixtures import BusinessRuleFactory2DB


@pytest.mark.parametrize("test_input, test_output", [
    (["BR1", "testquery", True],
     ["0, BR1, testquery, True"])
])
def test_business_rule_to_string(api_client, orm_client,
                                 test_input, test_output):
    business_rule = BusinessRuleFactory2DB(name=test_input[0],
                                           query=test_input[1],
                                           executing=test_input[2])

    assert business_rule.__str__() == test_output[0]


@pytest.mark.parametrize("test_input, test_output", [
    (["BR1", "testquery"],
     ["0, BR1, testquery, True"])
])
def test_business_rule_no_executing_to_string(api_client, orm_client,
                                              test_input, test_output):
    business_rule = BusinessRuleFactory2DB(name=test_input[0],
                                           query=test_input[1])

    assert business_rule.__str__() == test_output[0]
