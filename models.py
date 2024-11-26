from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    UserID = Column(Integer, primary_key=True, index=True)
    Email = Column(String, unique=True, index=True)
    Username = Column(String, index=True)

class Room(Base):
    __tablename__ = "rooms"
    RoomID = Column(Integer, primary_key=True, index=True)
    RoomName = Column(String, index=True)

class Course(Base):
    __tablename__ = "courses"
    CourseID = Column(Integer, primary_key=True, index=True)
    CourseName = Column(String, index=True)

class ScheduleTable(Base):
    __tablename__ = "schedule_table"
    ScheduleID = Column(Integer, primary_key=True, index=True)
    UserID = Column(Integer, ForeignKey("users.UserID"))
    RoomID = Column(Integer, ForeignKey("rooms.RoomID"))
    CourseID = Column(Integer, ForeignKey("courses.CourseID"))
    Schedule = Column(DateTime)
    Approval = Column(Boolean)

    user = relationship("User")
    room = relationship("Room")
    course = relationship("Course")
