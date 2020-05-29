import logging

import pytest

from api import create_app
from core import database
from fixtures import DeviceFactory2DB, DeviceCategoryFactory2DB, EventFactory2DB, \
    EventAFactory2DB, EventBFactory2DB, BusinessRuleFactory2DB, LocationFactory2DB
from utils import db_uri

logger = logging.getLogger(__name__)


@pytest.fixture(scope="module", autouse=True)
def api_client():
    SQLALCHEMY_SETTINGS = {
        "SQLALCHEMY_DATABASE_URI": db_uri,
        "SQLALCHEMY_TRACK_MODIFICATIONS": False
    }

    print("API_CLIENT START")
    app, db = create_app(settings=SQLALCHEMY_SETTINGS)
    DeviceFactory2DB._meta.sqlalchemy_session = db.session
    DeviceCategoryFactory2DB._meta.sqlalchemy_session = db.session
    EventFactory2DB._meta.sqlalchemy_session = db.session
    EventAFactory2DB._meta.sqlalchemy_session = db.session
    EventBFactory2DB._meta.sqlalchemy_session = db.session
    BusinessRuleFactory2DB._meta.sqlalchemy_session = db.session
    LocationFactory2DB._meta.sqlalchemy_session = db.session
    yield app.test_client()
    print("API_CLIENT END")
    db.session.close()
    db.engine.dispose()


@pytest.fixture(scope="function", autouse=True)
def clear_tables():
    print("CLEAR_TABLES START")
    yield
    session = database.session
    for name, table in database.metadata.tables.items():
        session.execute(f'ALTER TABLE "{table.name}" DISABLE TRIGGER ALL;')
        session.execute(table.delete())
        session.execute(f'ALTER TABLE "{table.name}" ENABLE TRIGGER ALL;')
    print("CLEAR_TABLES END")
    session.commit()
    session.close()


@pytest.fixture(scope="function")
def orm_client(api_client):
    client = database
    client.init_db()
    print("ORM_CLIENT START")
    yield client
    DeviceFactory2DB.reset_sequence(value=0, force=True)
    DeviceCategoryFactory2DB.reset_sequence(value=0, force=True)
    EventFactory2DB.reset_sequence(value=0, force=True)
    EventAFactory2DB.reset_sequence(value=0, force=True)
    EventBFactory2DB.reset_sequence(value=0, force=True)
    BusinessRuleFactory2DB.reset_sequence(value=0, force=True)
    LocationFactory2DB.reset_sequence(value=0, force=True)
    print("ORM_CLIENT END")
    client.close()
