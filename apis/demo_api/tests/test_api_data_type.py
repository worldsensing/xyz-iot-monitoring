import json

from repositories import api_repository


def test_get_data_types_all(api_client, orm_client):
    rv = api_client.get(f"/data-types/")
    assert rv.status_code == 200
    response_content = json.loads(rv.data)['data']
    assert response_content == api_repository.data_type
