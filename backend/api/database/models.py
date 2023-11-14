import enum

from database.database import base
from sqlalchemy import (TEXT, TIMESTAMP, Boolean, Column, Enum, ForeignKey,
                        Integer)


class UserTypes(enum.Enum):
    student = "student"
    teacher = "teacher"
    elder = "elder"
    moderator = "moderator"
    superadmin = "superadmin"
    

class FacilitySpec(enum.Enum):
    lecture = "lecture"
    lab_or_prac = "lab_or_prac"
    unknown = "unknown"
    

class Group(base):
    __tablename__ = "group"

    id = Column(Integer, primary_key=True)

    name = Column(TEXT, unique=True)
    num = Column(Integer, unique=True)

    subgroups_count = Column(Integer)
    
    
class SpecialEvent(base):
    __tablename__ = "special_group"
    
    id = Column(Integer, primary_key=True)
    
    name = Column(TEXT)
    group = Column(TEXT)
    rule = Column(TEXT)
    

class Subgroup(base):
    __tablename__ = "subgroup"
    
    id = Column(Integer, primary_key=True)
    
    name = Column(TEXT)
    group = Column(ForeignKey(Group.id))


class User(base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)

    name = Column(TEXT)
    
    type = Column(Enum(UserTypes), default='regular_user')

    email = Column(TEXT)
    
    color = Column(TEXT)
    theme = Column(TEXT)

    group = Column(ForeignKey(Group.id))
    subgroup = Column(TEXT)


class Facility(base):
    __tablename__ = "facility"

    id = Column(Integer, primary_key=True)

    name = Column(TEXT, unique=True)
    num = Column(Integer, unique=True)

    spec = Column(Enum(FacilitySpec))
    capacity = Column(Integer, default=0)


class Teacher(base):
    __tablename__ = "teacher"

    id = Column(TEXT, primary_key=True)

    name = Column(TEXT, unique=True)


class Event(base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True)

    name = Column(TEXT)
    order = Column(Integer)

    begin = Column(TIMESTAMP)
    end = Column(TIMESTAMP)

    facility = Column(TEXT)

    capacity = Column(Integer)
    teacher = Column(TEXT)

    group = Column(TEXT)
    subgroup = Column(TEXT)

    changed = Column(Boolean, default=False)