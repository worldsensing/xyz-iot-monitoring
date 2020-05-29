# -*- coding: utf-8 -*-
from flask_cors import CORS

from resources.api_handlers import DataTypeHandler, DeviceCategoryHandler, DeviceHandler, \
    EventHandler, BusinessRulesHandler, LocationsHandler


class Resources:
    def init_cors(app):
        cors_resources = [r'/device-categories/*', r'/devices/*', r'/events/*',
                          r'/business-rules/*', r'/locations/*']
        cors_origins = ["http://localhost:3000", "http://localhost:8000",
                        "https://editor.swagger.io"]

        CORS(app, resources=cors_resources, origins=cors_origins)

    @staticmethod
    def load_resources(api):
        api.add_resource(DataTypeHandler.DataTypes, '/data-types/',
                         strict_slashes=False)

        api.add_resource(DataTypeHandler.DataType, '/data-types/<string:data_type_name>',
                         strict_slashes=False)

        api.add_resource(DeviceCategoryHandler.DeviceCategories, '/device-categories/',
                         strict_slashes=False)

        api.add_resource(DeviceCategoryHandler.DeviceCategory,
                         '/device-categories/<string:device_category_name>',
                         strict_slashes=False)

        api.add_resource(DeviceHandler.Devices, '/devices/',
                         strict_slashes=False)

        api.add_resource(DeviceHandler.Device, '/devices/<string:device_name>',
                         strict_slashes=False)

        api.add_resource(DeviceHandler.DeviceEvent, '/devices/<string:device_name>/event/',
                         strict_slashes=False)

        api.add_resource(EventHandler.Events, '/events/',
                         strict_slashes=False)

        api.add_resource(EventHandler.Event, '/events/<string:event_id>',
                         strict_slashes=False)

        api.add_resource(BusinessRulesHandler.BusinessRules, '/business-rules/',
                         strict_slashes=False)

        api.add_resource(BusinessRulesHandler.BusinessRule,
                         '/business-rules/<string:business_rule_name>',
                         strict_slashes=False)

        api.add_resource(LocationsHandler.Locations, '/locations/',
                         strict_slashes=False)

        api.add_resource(LocationsHandler.Location, '/locations/<string:location_name>',
                         strict_slashes=False)
