# -*- coding: utf-8 -*-

from translators import model_translators


def device_category_translator(device_category_from_db):
    return {
        "id": device_category_from_db.id,
        "name": device_category_from_db.name,
        "data_type": device_category_from_db.data_type,
    }


def device_translator(device_from_db):
    return {
        "id": device_from_db.id,
        "name": device_from_db.name,
        "category": device_from_db.category,
        "location": device_from_db.location,
    }


def event_translator(event_from_db):
    return {
        "id": event_from_db.id,
        "device_name": event_from_db.device_name,
        "value": event_from_db.value,
        "datetime": model_translators.translate_datetime(event_from_db.datetime),
    }


def business_rule_translator(business_rule_from_db):
    return {
        "id": business_rule_from_db.id,
        "name": business_rule_from_db.name,
        "query": business_rule_from_db.query,
        "executing": business_rule_from_db.executing,
    }


def location_translator(location_from_db):
    return {
        "id": location_from_db.id,
        "name": location_from_db.name,
        "latlng": location_from_db.latlng,
    }
