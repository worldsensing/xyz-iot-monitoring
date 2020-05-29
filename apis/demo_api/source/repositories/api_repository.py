# -*- coding: utf-8 -*-
from core import database

from models.models import data_type


class ApiRepository:
    @staticmethod
    def get_all_data_types():
        return data_type

    @staticmethod
    def add_device_category(device_category):
        return database.add_device_category(device_category)

    @staticmethod
    def get_all_device_categories():
        return database.get_all_device_categories()

    @staticmethod
    def get_device_category(device_category_name):
        return database.get_device_category(device_category_name)

    @staticmethod
    def update_device_category(device_category_name, device_category):
        return database.update_device_category(device_category_name, device_category)

    @staticmethod
    def delete_device_category(device_category_name):
        return database.delete_device_category(device_category_name)

    @staticmethod
    def add_device(device):
        return database.add_device(device)

    @staticmethod
    def get_all_devices():
        return database.get_all_devices()

    @staticmethod
    def get_device(device_name):
        return database.get_device(device_name)

    @staticmethod
    def update_device(device_name, device):
        return database.update_device(device_name, device)

    @staticmethod
    def delete_device(device_name):
        return database.delete_device(device_name)

    @staticmethod
    def get_devices_with_device_category(device_category):
        return database.get_devices_with_device_category(device_category)

    @staticmethod
    def get_events_for_device(device_name):
        return database.get_events_for_device(device_name)

    @staticmethod
    def add_event(event):
        return database.add_event(event)

    @staticmethod
    def get_all_events():
        return database.get_all_events()

    @staticmethod
    def get_event(event_id):
        return database.get_event(event_id)

    @staticmethod
    def delete_event(event_id):
        return database.delete_event(event_id)

    @staticmethod
    def add_business_rule(business_rule):
        return database.add_business_rule(business_rule)

    @staticmethod
    def get_all_business_rules():
        return database.get_all_business_rules()

    @staticmethod
    def get_business_rule(business_rule_name):
        return database.get_business_rule(business_rule_name)

    @staticmethod
    def update_business_rule(business_rule_name, business_rule):
        return database.update_business_rule(business_rule_name, business_rule)

    @staticmethod
    def delete_business_rule(business_rule_name):
        return database.delete_business_rule(business_rule_name)

    @staticmethod
    def add_location(location):
        return database.add_location(location)

    @staticmethod
    def get_all_locations():
        return database.get_all_locations()

    @staticmethod
    def get_location(location_name):
        return database.get_location(location_name)

    @staticmethod
    def update_location(location_name, location):
        return database.update_location(location_name, location)

    @staticmethod
    def delete_location(location_name):
        return database.delete_location(location_name)
