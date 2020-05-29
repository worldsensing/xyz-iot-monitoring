# -*- coding: utf-8 -*-
import enum

from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime, UniqueConstraint, \
    Enum, Boolean
from sqlalchemy.orm import relationship

from core.database import Base
from translators import model_translators

data_type = ["event_a", "event_b"]


class DataTypeEnum(str, enum.Enum):
    EventA = data_type[0]
    EventB = data_type[1]


class Device(Base):
    __tablename__ = "device"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(32), unique=True, nullable=False)
    category = Column(String(32), ForeignKey('device_category.name', ondelete="SET NULL"),
                      nullable=False)
    location = Column(String(32), ForeignKey('location.name', ondelete="SET NULL"))
    events = relationship('Event')

    def __str__(self):
        return f"{self.id}, {self.name}, {self.category}, {self.location}"


class DeviceCategory(Base):
    __tablename__ = "device_category"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(32), unique=True, nullable=False)
    data_type = Column(Enum(DataTypeEnum), nullable=False)
    devices = relationship('Device')

    def __str__(self):
        return f"{self.id}, {self.name}, {self.data_type}"


class Event(Base):
    __tablename__ = "event"
    id = Column(Integer, primary_key=True, nullable=False)
    device_name = Column(String(32), ForeignKey('device.name', ondelete="cascade"))
    datetime = Column(DateTime(timezone=True), nullable=False)
    type = Column(String(8))

    UniqueConstraint('device_name', 'datetime')

    __mapper_args__ = {
        'polymorphic_identity': 'event',
        'polymorphic_on': type
    }


class EventA(Event):
    __tablename__ = "event_a"
    id = Column(Integer, ForeignKey('event.id', ondelete="cascade"), primary_key=True)
    value = Column(String(32), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'event_a',
    }

    def __str__(self):
        return f"{self.id}, {self.device_name}, {self.value}, " \
               f"{model_translators.translate_datetime(self.datetime)}"


class EventB(Event):
    __tablename__ = "event_b"
    id = Column(Integer, ForeignKey('event.id', ondelete="cascade"), primary_key=True)
    value = Column(Float, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'event_b',
    }

    def __str__(self):
        return f"{self.id}, {self.device_name}, {self.value}, " \
               f"{model_translators.translate_datetime(self.datetime)}"


class BusinessRule(Base):
    __tablename__ = "business_rule"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(32), unique=True, nullable=False)
    query = Column(String(256), nullable=False)
    executing = Column(Boolean, default=True)

    def __str__(self):
        return f"{self.id}, {self.name}, {self.query}, {self.executing}"


class Location(Base):
    __tablename__ = "location"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(32), unique=True, nullable=False)
    latlng = Column(String(32))
    devices = relationship('Device')

    def __str__(self):
        return f"{self.id}, {self.name}, {self.latlng}"
