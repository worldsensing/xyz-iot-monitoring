# -*- coding: utf-8 -*-
import logging

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from utils import db_uri

logger = logging.getLogger(__name__)

engine = create_engine(db_uri, convert_unicode=True)
session = scoped_session(sessionmaker(autocommit=False,
                                      autoflush=True,
                                      bind=engine))

Base = declarative_base()
Base.query = session.query_property()
metadata = Base.metadata


def init_db():
    Base.metadata.create_all(engine, checkfirst=True)


def add_device_category(device_category):
    try:
        session.add(device_category)
        session.flush()
        name = device_category.name
        session.commit()
    except:
        session.rollback()
        return None

    return name


def get_all_device_categories():
    from models.models import DeviceCategory

    try:
        device_categories = session.query(DeviceCategory) \
            .all()
        session.commit()
    except:
        session.rollback()
        return None

    return device_categories


def get_device_category(device_category_name):
    from models.models import DeviceCategory

    try:
        device_categories = session.query(DeviceCategory) \
            .filter_by(name=device_category_name) \
            .first()
        session.commit()
    except:
        session.rollback()
        return None

    return device_categories


def update_device_category(device_category_name, device_category):
    from models.models import DeviceCategory

    try:
        session.query(DeviceCategory) \
            .filter_by(name=device_category_name) \
            .update(device_category)
        session.commit()
    except:
        session.rollback()
        return None

    return device_category_name


def delete_device_category(device_category_name):
    from models.models import DeviceCategory

    try:
        session.query(DeviceCategory) \
            .filter_by(name=device_category_name) \
            .delete()
        session.commit()
    except:
        session.rollback()
        return None

    return device_category_name


def add_device(device):
    try:
        session.add(device)
        session.flush()
        name = device.name
        session.commit()
    except:
        session.rollback()
        return None

    return name


def get_all_devices():
    from models.models import Device

    try:
        devices = session.query(Device) \
            .all()
        session.commit()
    except:
        session.rollback()
        return None

    return devices


def get_device(device_name):
    from models.models import Device

    try:
        device = session.query(Device) \
            .filter_by(name=device_name) \
            .first()
        session.commit()
    except:
        session.rollback()
        return None

    return device


def update_device(device_name, device):
    from models.models import Device

    try:
        session.query(Device) \
            .filter_by(name=device_name) \
            .update(device)
        session.commit()
    except:
        session.rollback()
        return None

    return device_name


def delete_device(device_name):
    from models.models import Device

    try:
        session.query(Device) \
            .filter_by(name=device_name) \
            .delete()
        session.commit()
    except:
        session.rollback()
        return None

    return device_name


def get_devices_with_device_category(device_category):
    from models.models import Device

    try:
        devices = session.query(Device) \
            .filter_by(category=device_category) \
            .all()
        session.commit()
    except:
        session.rollback()
        return None

    return devices


def get_events_for_device(device_name):
    from models.models import Event

    try:
        events = session.query(Event) \
            .filter_by(device_name=device_name) \
            .all()
        session.commit()
    except:
        session.rollback()
        return None

    return events


def add_event(event):
    try:
        session.add(event)
        session.flush()
        id = event.id
        session.commit()
    except:
        session.rollback()
        return None

    return id


def get_all_events():
    from models.models import Event

    events = None
    try:
        events = session.query(Event) \
            .all()
        session.commit()
    except:
        session.rollback()

    return events


def get_event(event_id):
    from models.models import Event

    try:
        event = session.query(Event) \
            .filter_by(id=event_id) \
            .first()
        session.commit()
    except:
        session.rollback()
        return None

    return event


def delete_event(event_id):
    from models.models import Event

    try:
        session.query(Event) \
            .filter_by(id=event_id) \
            .delete()
        session.commit()
    except:
        session.rollback()
        return None

    return event_id


def add_business_rule(business_rule):
    try:
        session.add(business_rule)
        session.flush()
        name = business_rule.name
        session.commit()
    except:
        session.rollback()
        return None

    return name


def get_all_business_rules():
    from models.models import BusinessRule

    try:
        business_rules = session.query(BusinessRule) \
            .all()
        session.commit()
    except:
        session.rollback()
        return None

    return business_rules


def get_business_rule(business_rule_name):
    from models.models import BusinessRule

    try:
        business_rules = session.query(BusinessRule) \
            .filter_by(name=business_rule_name) \
            .first()
        session.commit()
    except:
        session.rollback()
        return None

    return business_rules


def update_business_rule(business_rule_name, business_rule):
    from models.models import BusinessRule

    try:
        session.query(BusinessRule) \
            .filter_by(name=business_rule_name) \
            .update(business_rule)
        session.commit()
    except Exception as e:
        session.rollback()
        return None

    return business_rule_name


def delete_business_rule(business_rule_name):
    from models.models import BusinessRule

    try:
        session.query(BusinessRule) \
            .filter_by(name=business_rule_name) \
            .delete()
        session.commit()
    except:
        session.rollback()
        return None

    return business_rule_name


def add_location(location):
    try:
        session.add(location)
        session.flush()
        name = location.name
        session.commit()
    except:
        session.rollback()
        return None

    return name


def get_all_locations():
    from models.models import Location

    try:
        locations = session.query(Location) \
            .all()
        session.commit()
    except:
        session.rollback()
        return None

    return locations


def get_location(location_name):
    from models.models import Location

    try:
        locations = session.query(Location) \
            .filter_by(name=location_name) \
            .first()
        session.commit()
    except:
        session.rollback()
        return None

    return locations


def update_location(location_name, location):
    from models.models import Location

    try:
        session.query(Location) \
            .filter_by(name=location_name) \
            .update(location)
        session.commit()
    except Exception as e:
        session.rollback()
        return None

    return location_name


def delete_location(location_name):
    from models.models import Location

    try:
        session.query(Location) \
            .filter_by(name=location_name) \
            .delete()
        session.commit()
    except:
        session.rollback()
        return None

    return location_name


def close():
    session.close()
    engine.dispose()
