import logging

from flask_restful import reqparse

from errors.api_errors import GENERIC, NOT_EXISTS_ID, FIELD_NOT_VALID, NOT_EXISTS_DEVICE, \
    NOT_DEVICE_CATEGORY, DEVICE_CATEGORY_HAS_DEVICE, EXISTS_ID, NOT_EXISTS_LOCATION
from models.models import Device, EventB, EventA, DeviceCategory, DataTypeEnum, BusinessRule, \
    Location
from resources import Resource, Response
from translators import api_translators as translator
from validators.api_validators import DeviceValidator, EventValidator, DeviceCategoryValidator, \
    BusinessRuleValidator, LocationValidator

logger = logging.getLogger(__name__)

device_category_parser = reqparse.RequestParser()
device_category_parser.add_argument("name", type=str)
device_category_parser.add_argument("data_type", type=str)

device_parser = reqparse.RequestParser()
device_parser.add_argument("name", type=str)
device_parser.add_argument("category", type=str)
device_parser.add_argument("location", type=str, required=False)

event_parser = reqparse.RequestParser()
event_parser.add_argument("device_name", type=str)
event_parser.add_argument("value", type=str)
event_parser.add_argument("datetime", type=str)

business_rule_parser = reqparse.RequestParser()
business_rule_parser.add_argument("name", type=str)
business_rule_parser.add_argument("query", type=str)
business_rule_parser.add_argument("executing", type=bool, required=False)

location_parser = reqparse.RequestParser()
location_parser.add_argument("name", type=str)
location_parser.add_argument("latlng", type=str, required=False)


class DataTypeHandler:
    class DataTypes(Resource):
        def get(self):
            response = self.repository.get_all_data_types()

            return Response.success(response)

    class DataType(Resource):
        def get(self, data_type_name):
            response = self.repository.get_data_type(data_type_name)

            if response:
                return Response.success(response)

            return Response.error(NOT_EXISTS_ID)


class DeviceCategoryHandler:
    class DeviceCategories(Resource):
        def get(self):
            response = self.repository.get_all_device_categories()

            return Response.success(
                [translator.device_category_translator(device_category)
                 for device_category in response])

        def post(self):
            args = device_category_parser.parse_args()

            # Get DeviceCategory arguments
            if DeviceCategoryValidator.is_name_valid(args["name"]):
                name = args["name"]

                response = self.repository.get_device_category(name)
                if response:
                    return Response.error(EXISTS_ID)
            else:
                return Response.error(FIELD_NOT_VALID)

            if DeviceCategoryValidator.is_data_type_valid(args["data_type"]):
                data_type = args["data_type"]
            else:
                return Response.error(FIELD_NOT_VALID)

            device_category = DeviceCategory(name=name, data_type=data_type)

            result = self.repository.add_device_category(device_category)
            if result:
                return Response.success({"name": result})

            return Response.error(GENERIC)

    class DeviceCategory(Resource):
        def get(self, device_category_name):
            response = self.repository.get_device_category(device_category_name)

            if response:
                return Response.success(translator.device_category_translator(response))
            return Response.error(NOT_EXISTS_ID)

        # TODO Only changes are possible in Name, not in data_type
        def put(self, device_category_name):
            args = device_category_parser.parse_args()

            response = self.repository.get_device_category(device_category_name)
            if response is None:
                return Response.error(NOT_EXISTS_ID)

            # Get DeviceCategory arguments
            if DeviceCategoryValidator.is_name_valid(args["name"]):
                name = args["name"]
            else:
                return Response.error(FIELD_NOT_VALID)

            if DeviceCategoryValidator.is_data_type_valid(args["data_type"]):
                data_type = args["data_type"]
            else:
                return Response.error(FIELD_NOT_VALID)

            device = {
                "name": name,
                "data_type": data_type
            }

            response = self.repository.update_device_category(device_category_name, device)
            if response:
                return Response.success({"name": response})

            return Response.error(GENERIC)

        def delete(self, device_category_name):
            response = self.repository.get_device_category(device_category_name)

            if response is None:
                return Response.error(NOT_EXISTS_ID)

            response = self.repository.get_devices_with_device_category(device_category_name)
            if response:
                return Response.error(DEVICE_CATEGORY_HAS_DEVICE)

            result = self.repository.delete_device_category(device_category_name)
            if result:
                return Response.success({"name": result})
            return Response.error(GENERIC)


class DeviceHandler:
    class Devices(Resource):
        def get(self):
            response = self.repository.get_all_devices()

            return Response.success(
                [translator.device_translator(device) for device in response])

        def post(self):
            args = device_parser.parse_args()

            # Get Device arguments
            if DeviceValidator.is_name_valid(args["name"]):
                name = args["name"]

                response = self.repository.get_device(name)
                if response:
                    return Response.error(EXISTS_ID)
            else:
                return Response.error(FIELD_NOT_VALID)

            if DeviceValidator.is_category_valid(args["category"]):
                category = args["category"]

                response = self.repository.get_device_category(category)
                if response is None:
                    return Response.error(NOT_DEVICE_CATEGORY)
            else:
                return Response.error(FIELD_NOT_VALID)

            if DeviceValidator.is_location_valid(args["location"]):
                location = args["location"]

                response = self.repository.get_location(location)
                if response is None:
                    return Response.error(NOT_EXISTS_LOCATION)
            else:
                location = None

            device = Device(name=name, category=category, location=location)

            result = self.repository.add_device(device)
            if result:
                return Response.success({"name": result})

            return Response.error(GENERIC)

    class Device(Resource):
        def get(self, device_name):
            response = self.repository.get_device(device_name)

            if response:
                return Response.success(translator.device_translator(response))
            return Response.error(NOT_EXISTS_ID)

        def put(self, device_name):
            args = device_parser.parse_args()

            response = self.repository.get_device(device_name)
            if response is None:
                return Response.error(NOT_EXISTS_ID)

            # Get Device arguments
            if DeviceValidator.is_name_valid(args["name"]):
                name = args["name"]
            else:
                return Response.error(FIELD_NOT_VALID)

            if DeviceValidator.is_category_valid(args["category"]):
                category = args["category"]
            else:
                return Response.error(FIELD_NOT_VALID)

            if DeviceValidator.is_location_valid(args["location"]):
                location = args["location"]
            else:
                return Response.error(FIELD_NOT_VALID)

            device = {
                "name": name,
                "category": category,
                "location": location
            }

            response = self.repository.update_device(device_name, device)
            if response:
                return Response.success({"name": response})

            return Response.error(GENERIC)

        def delete(self, device_name):
            response = self.repository.get_device(device_name)

            if response is None:
                return Response.error(NOT_EXISTS_ID)

            result = self.repository.delete_device(device_name)
            if result:
                return Response.success({"name": result})
            return Response.error(GENERIC)

    class DeviceEvent(Resource):
        def get(self, device_name):
            response = self.repository.get_device(device_name)
            if response is None:
                return Response.error(NOT_EXISTS_ID)

            response = self.repository.get_events_for_device(device_name)

            return Response.success(
                [translator.event_translator(event) for event in response])


class EventHandler:
    class Events(Resource):
        def get(self):
            response = self.repository.get_all_events()

            return Response.success(
                [translator.event_translator(event) for event in response])

        def post(self):
            args = event_parser.parse_args()

            # Get Event arguments
            if EventValidator.is_device_name_valid(args["device_name"]):
                device_name = args["device_name"]

                device = self.repository.get_device(device_name)
                if not device:
                    return Response.error(NOT_EXISTS_DEVICE)
            else:
                return Response.error(FIELD_NOT_VALID)

            if EventValidator.is_value_valid(args["value"]):
                value = args["value"]
            else:
                return Response.error(FIELD_NOT_VALID)

            if EventValidator.is_date_valid(args["datetime"]):
                datetime = args["datetime"]
            else:
                return Response.error(FIELD_NOT_VALID)

            device_category_name = device.category
            if device_category_name is None:
                return Response.error(NOT_DEVICE_CATEGORY)

            device_category = self.repository.get_device_category(device_category_name)
            if device_category is None:
                return Response.error(NOT_DEVICE_CATEGORY)

            device_category_data_type = device_category.data_type
            if device_category_data_type is None:
                return Response.error(NOT_DEVICE_CATEGORY)

            event = None
            if device_category_data_type == DataTypeEnum.EventA:
                event = EventA(device_name=device_name, value=value, datetime=datetime)
            elif device_category_data_type == DataTypeEnum.EventB:
                event = EventB(device_name=device_name, value=value, datetime=datetime)

            if event is None:
                return Response.error(GENERIC)

            result = self.repository.add_event(event)
            if result:
                return Response.success({"id": result})

            return Response.error(GENERIC)

    class Event(Resource):
        def get(self, event_id):
            response = self.repository.get_event(event_id)

            if response:
                return Response.success(translator.event_translator(response))
            return Response.error(NOT_EXISTS_ID)

        def delete(self, event_id):
            response = self.repository.get_event(event_id)

            if response is None:
                return Response.error(NOT_EXISTS_ID)

            result = self.repository.delete_event(event_id)
            if result:
                return Response.success({"id": result})

            return Response.error(GENERIC)


class BusinessRulesHandler:
    class BusinessRules(Resource):
        def get(self):
            response = self.repository.get_all_business_rules()

            return Response.success(
                [translator.business_rule_translator(business_rule)
                 for business_rule in response])

        def post(self):
            args = business_rule_parser.parse_args()

            # Get BusinessRule arguments
            if BusinessRuleValidator.is_name_valid(args["name"]):
                name = args["name"]

                response = self.repository.get_business_rule(name)
                if response:
                    return Response.error(EXISTS_ID)
            else:
                return Response.error(FIELD_NOT_VALID)

            if BusinessRuleValidator.is_query_valid(args["query"]):
                query = args["query"]
            else:
                return Response.error(FIELD_NOT_VALID)

            if BusinessRuleValidator.is_executing_valid(args["executing"]):
                executing = args["executing"]
            else:
                executing = True

            business_rule = BusinessRule(name=name, query=query, executing=executing)

            result = self.repository.add_business_rule(business_rule)
            if result:
                return Response.success({"name": result})

            return Response.error(GENERIC)

    class BusinessRule(Resource):
        def get(self, business_rule_name):
            response = self.repository.get_business_rule(business_rule_name)

            if response:
                return Response.success(translator.business_rule_translator(response))
            return Response.error(NOT_EXISTS_ID)

        # TODO Only changes are possible in query, not in device_name nor name
        def put(self, business_rule_name):
            args = business_rule_parser.parse_args()

            response = self.repository.get_business_rule(business_rule_name)
            if response is None:
                return Response.error(NOT_EXISTS_ID)

            # Get BusinessRule arguments
            if BusinessRuleValidator.is_name_valid(args["name"]):
                name = args["name"]

                response = self.repository.get_business_rule(name)
                if response is None:
                    return Response.error(EXISTS_ID)
            else:
                return Response.error(FIELD_NOT_VALID)

            if BusinessRuleValidator.is_query_valid(args["query"]):
                query = args["query"]
            else:
                return Response.error(FIELD_NOT_VALID)

            if BusinessRuleValidator.is_executing_valid(args["executing"]):
                executing = args["executing"]
            else:
                executing = True

            business_rule = {
                "name": name,
                "query": query,
                "executing": executing
            }

            response = self.repository.update_business_rule(business_rule_name, business_rule)
            if response:
                return Response.success({"name": response})

            return Response.error(GENERIC)

        def delete(self, business_rule_name):
            response = self.repository.get_business_rule(business_rule_name)

            if response is None:
                return Response.error(NOT_EXISTS_ID)

            result = self.repository.delete_business_rule(business_rule_name)
            if result:
                return Response.success({"name": result})
            return Response.error(GENERIC)


class LocationsHandler:
    class Locations(Resource):
        def get(self):
            response = self.repository.get_all_locations()

            return Response.success(
                [translator.location_translator(location)
                 for location in response])

        def post(self):
            args = location_parser.parse_args()

            # Get Location arguments
            if LocationValidator.is_name_valid(args["name"]):
                name = args["name"]

                response = self.repository.get_location(name)
                if response:
                    return Response.error(EXISTS_ID)
            else:
                return Response.error(FIELD_NOT_VALID)

            if LocationValidator.is_latlng_valid(args["latlng"]):
                latlng = args["latlng"]
            else:
                latlng = None

            location = Location(name=name, latlng=latlng)

            result = self.repository.add_location(location)
            if result:
                return Response.success({"name": result})

            return Response.error(GENERIC)

    class Location(Resource):
        def get(self, location_name):
            response = self.repository.get_location(location_name)

            if response:
                return Response.success(translator.location_translator(response))
            return Response.error(NOT_EXISTS_ID)

        # TODO Only changes are possible in query, not in device_name nor name
        def put(self, location_name):
            args = location_parser.parse_args()

            # Get Location arguments
            if LocationValidator.is_name_valid(args["name"]):
                name = args["name"]

                response = self.repository.get_location(name)
                if response is None:
                    return Response.error(NOT_EXISTS_ID)
            else:
                return Response.error(FIELD_NOT_VALID)

            if LocationValidator.is_latlng_valid(args["latlng"]):
                latlng = args["latlng"]
            else:
                latlng = None

            location = {
                "name": name,
                "latlng": latlng,
            }

            response = self.repository.update_location(location_name, location)
            if response:
                return Response.success({"name": response})

            return Response.error(GENERIC)

        def delete(self, location_name):
            response = self.repository.get_location(location_name)

            if response is None:
                return Response.error(NOT_EXISTS_ID)

            result = self.repository.delete_location(location_name)
            if result:
                return Response.success({"name": result})
            return Response.error(GENERIC)
