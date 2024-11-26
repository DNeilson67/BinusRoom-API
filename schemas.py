from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    Email: str
    Username: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    UserID: int
    class Config:
        orm_mode = True

class RoomBase(BaseModel):
    RoomName: str

class RoomCreate(RoomBase):
    pass

class Room(RoomBase):
    RoomID: int
    class Config:
        orm_mode = True

class CourseBase(BaseModel):
    CourseName: str

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    CourseID: int
    class Config:
        orm_mode = True

class ScheduleBase(BaseModel):
    UserID: int
    RoomID: int
    CourseID: int
    Schedule: datetime
    Approval: bool

class ScheduleCreate(ScheduleBase):
    pass

class Schedule(ScheduleBase):
    ScheduleID: int
    class Config:
        orm_mode = True
