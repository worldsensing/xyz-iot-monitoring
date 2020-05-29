from models.models import data_type


class DeviceCategoryValidator:
    @staticmethod
    def is_name_valid(value):
        return isinstance(value, str) and not value == ""

    @staticmethod
    def is_data_type_valid(value):
        return isinstance(value, str) and value in data_type


class DeviceValidator:
    @staticmethod
    def is_name_valid(value):
        return isinstance(value, str) and not value == ""

    @staticmethod
    def is_category_valid(value):
        return isinstance(value, str) and not value == ""

    @staticmethod
    def is_location_valid(value):
        return isinstance(value, str) and not value == ""


class EventValidator:
    @staticmethod
    def is_device_name_valid(value):
        return isinstance(value, str) and not value == ""

    @staticmethod
    def is_value_valid(value):
        return isinstance(value, str) and not value == ""

    @staticmethod
    def is_date_valid(value):
        return isinstance(value, str) and not value == ""


class BusinessRuleValidator:
    @staticmethod
    def is_name_valid(value):
        return isinstance(value, str) and not value == ""

    @staticmethod
    def is_query_valid(value):
        return isinstance(value, str) and not value == ""

    @staticmethod
    def is_executing_valid(value):
        return isinstance(value, bool)


class LocationValidator:
    @staticmethod
    def is_name_valid(value):
        return isinstance(value, str) and not value == ""

    @staticmethod
    def is_latlng_valid(value):
        return isinstance(value, str) and not value == "" and len(value.split(",")) == 2
