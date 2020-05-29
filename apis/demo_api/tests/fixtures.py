import datetime
from functools import partial

import factory
from dateutil.tz import UTC
from factory.fuzzy import FuzzyDateTime

from models.models import Device, DeviceCategory, Event, EventA, EventB, BusinessRule, Location


def dict_factory(factory, **kwargs):
    return factory.stub(**kwargs).__dict__


class AbstractDeviceFactory(factory.Factory):
    class Meta:
        model = Device
        abstract = True

    id = factory.Sequence(lambda n: int(n))
    name = "a"
    category = "Inclinometer"
    location = None  # "MyLocation1"


class DeviceFactory(AbstractDeviceFactory):
    pass


DeviceFactory._meta.exclude = ("id",)
DeviceDictFactory = partial(dict_factory, DeviceFactory)


class DeviceFactory2DB(AbstractDeviceFactory, factory.alchemy.SQLAlchemyModelFactory):
    """Elements created with this factory are inserted in the DB"""

    class Meta:
        # NOTE Session is assigned on conftest
        sqlalchemy_session_persistence = "commit"


class AbstractDeviceCategoryFactory(factory.Factory):
    class Meta:
        model = DeviceCategory
        abstract = True

    id = factory.Sequence(lambda n: int(n))
    name = "Inclinometer"
    data_type = "event_a"


class DeviceCategoryFactory(AbstractDeviceCategoryFactory):
    pass


DeviceCategoryFactory._meta.exclude = ("id",)
DeviceCategoryDictFactory = partial(dict_factory, DeviceCategoryFactory)


class DeviceCategoryFactory2DB(AbstractDeviceCategoryFactory,
                               factory.alchemy.SQLAlchemyModelFactory):
    """Elements created with this factory are inserted in the DB"""

    class Meta:
        # NOTE Session is assigned on conftest
        sqlalchemy_session_persistence = "commit"


class AbstractEventFactory(factory.Factory):
    class Meta:
        model = Event
        abstract = True

    id = factory.Sequence(lambda n: int(n))
    device_name = "a"
    # datetime = "2020-03-18T12:00:00+00:00"
    datetime = FuzzyDateTime(datetime.datetime(2019, 1, 1, tzinfo=UTC),
                             datetime.datetime(2020, 1, 1, tzinfo=UTC),
                             force_microsecond=0)


class EventFactory(AbstractEventFactory):
    pass


EventFactory._meta.exclude = ("id",)
EventDictFactory = partial(dict_factory, EventFactory)


class EventFactory2DB(AbstractEventFactory, factory.alchemy.SQLAlchemyModelFactory):
    """Elements created with this factory are inserted in the DB"""

    class Meta:
        # NOTE Session is assigned on conftest
        sqlalchemy_session_persistence = "commit"


class AbstractEventAFactory(AbstractEventFactory):
    class Meta:
        model = EventA
        abstract = True

    id = factory.Sequence(lambda n: int(n))
    value = "0.0"


class EventAFactory(AbstractEventAFactory):
    pass


EventAFactory._meta.exclude = ("id",)
EventADictFactory = partial(dict_factory, EventAFactory)


class EventAFactory2DB(AbstractEventAFactory, factory.alchemy.SQLAlchemyModelFactory):
    """Elements created with this factory are inserted in the DB"""

    class Meta:
        # NOTE Session is assigned on conftest
        sqlalchemy_session_persistence = "commit"


class AbstractEventBFactory(AbstractEventFactory):
    class Meta:
        model = EventB
        abstract = True

    id = factory.Sequence(lambda n: int(n))
    value = 0.1


class EventBFactory(AbstractEventBFactory):
    pass


EventBFactory._meta.exclude = ("id",)
EventBDictFactory = partial(dict_factory, EventBFactory)


class EventBFactory2DB(AbstractEventBFactory, factory.alchemy.SQLAlchemyModelFactory):
    """Elements created with this factory are inserted in the DB"""

    class Meta:
        # NOTE Session is assigned on conftest
        sqlalchemy_session_persistence = "commit"


class AbstractBusinessRuleFactory(factory.Factory):
    class Meta:
        model = BusinessRule
        abstract = True

    id = factory.Sequence(lambda n: int(n))
    name = "BR1"
    query = "testquery"
    executing = None  # True


class BusinessRuleFactory(AbstractBusinessRuleFactory):
    pass


BusinessRuleFactory._meta.exclude = ("id",)
BusinessRuleDictFactory = partial(dict_factory, BusinessRuleFactory)


class BusinessRuleFactory2DB(AbstractBusinessRuleFactory, factory.alchemy.SQLAlchemyModelFactory):
    """Elements created with this factory are inserted in the DB"""

    class Meta:
        # NOTE Session is assigned on conftest
        sqlalchemy_session_persistence = "commit"


class AbstractLocationFactory(factory.Factory):
    class Meta:
        model = Location
        abstract = True

    id = factory.Sequence(lambda n: int(n))
    name = "Location1"
    latlng = None  # "41.2, 2.1"


class LocationFactory(AbstractLocationFactory):
    pass


LocationFactory._meta.exclude = ("id",)
LocationDictFactory = partial(dict_factory, LocationFactory)


class LocationFactory2DB(AbstractLocationFactory, factory.alchemy.SQLAlchemyModelFactory):
    """Elements created with this factory are inserted in the DB"""

    class Meta:
        # NOTE Session is assigned on conftest
        sqlalchemy_session_persistence = "commit"
