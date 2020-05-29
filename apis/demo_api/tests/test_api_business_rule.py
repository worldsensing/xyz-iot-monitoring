import json

import pytest

from fixtures import BusinessRuleFactory2DB, BusinessRuleDictFactory
from models.models import BusinessRule


def assert_business_rules(business_rule_api, business_rule_db):
    # assert business_rule_db["id"] == business_rule_api["id"]
    assert business_rule_db["name"] == business_rule_api["name"]
    assert business_rule_db["query"] == business_rule_api["query"]
    assert business_rule_db["executing"] == business_rule_api["executing"]


@pytest.mark.parametrize("test_input, test_input_2", [
    (["BR1", "query1", True],
     ["BR2", "query2", False])
])
def test_get_business_rules_all(api_client, orm_client,
                                test_input, test_input_2):
    assert orm_client.session.query(BusinessRule).count() == 0
    business_rule_1 = BusinessRuleFactory2DB(name=test_input[0],
                                             query=test_input[1],
                                             executing=test_input[2])
    assert orm_client.session.query(BusinessRule).count() == 1
    business_rule_2 = BusinessRuleFactory2DB(name=test_input_2[0],
                                             query=test_input_2[1],
                                             executing=test_input_2[2])
    assert orm_client.session.query(BusinessRule).count() == 2

    rv = api_client.get(f"/business-rules/")
    assert rv.status_code == 200
    response_content_1 = json.loads(rv.data)['data'][0]
    response_content_2 = json.loads(rv.data)['data'][1]
    assert_business_rules(response_content_1, business_rule_1.__dict__)
    assert_business_rules(response_content_2, business_rule_2.__dict__)


@pytest.mark.parametrize("test_input", [
    (["BR1", "query1", True])
])
def test_get_business_rule(api_client, orm_client,
                           test_input):
    assert orm_client.session.query(BusinessRule).count() == 0
    business_rule_1 = BusinessRuleFactory2DB(name=test_input[0],
                                             query=test_input[1],
                                             executing=test_input[2])
    assert orm_client.session.query(BusinessRule).count() == 1

    rv = api_client.get(f"/business-rules/{business_rule_1.name}")
    assert rv.status_code == 200
    response_content = json.loads(rv.data)['data']
    assert_business_rules(response_content, business_rule_1.__dict__)


@pytest.mark.parametrize("test_input", [
    (["BR1", "query1", True])
])
def test_add_business_rule(api_client, orm_client,
                           test_input):
    assert orm_client.session.query(BusinessRule).count() == 0
    business_rule_1 = BusinessRuleDictFactory(name=test_input[0],
                                              query=test_input[1],
                                              executing=test_input[2])
    assert orm_client.session.query(BusinessRule).count() == 0

    rv = api_client.post("/business-rules/", json=business_rule_1)
    assert rv.status_code == 200, rv.data
    response_content = json.loads(rv.data)['data']['name']

    # TODO Change to orm_client.session.query...
    rv = api_client.get(f"/business-rules/{response_content}")
    assert rv.status_code == 200
    response_content = json.loads(rv.data)['data']
    assert_business_rules(response_content, business_rule_1)


@pytest.mark.parametrize("test_input, test_modify", [
    (["BR1", "query1", True],
     ["BR1", "query1", False],)
])
def test_update_business_rule(api_client, orm_client,
                              test_input, test_modify):
    assert orm_client.session.query(BusinessRule).count() == 0
    business_rule_1 = BusinessRuleFactory2DB(name=test_input[0],
                                             query=test_input[1],
                                             executing=test_input[2])
    assert orm_client.session.query(BusinessRule).count() == 1

    business_rule_to_modify = BusinessRuleDictFactory(name=test_modify[0],
                                                      query=test_modify[1],
                                                      executing=test_modify[2])

    rv = api_client.put(f"/business-rules/{business_rule_1.name}",
                        json=business_rule_to_modify)
    assert rv.status_code == 200
    assert orm_client.session.query(BusinessRule).count() == 1

    rv = api_client.get(f"/business-rules/{business_rule_1.name}")
    assert rv.status_code == 200
    response_content = json.loads(rv.data)['data']
    assert_business_rules(response_content, business_rule_to_modify)


@pytest.mark.parametrize("test_input", [
    (["BR1", "query1", True])
])
def test_delete_business_rule(api_client, orm_client,
                              test_input):
    assert orm_client.session.query(BusinessRule).count() == 0
    business_rule_1 = BusinessRuleFactory2DB(name=test_input[0],
                                             query=test_input[1],
                                             executing=test_input[2])
    assert orm_client.session.query(BusinessRule).count() == 1

    rv = api_client.delete(f"/business-rules/{business_rule_1.name}")
    assert rv.status_code == 200

    assert orm_client.session.query(BusinessRule).count() == 0
