from sqlalchemy.orm import Session
import models, schemas

# USER CRUD
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.UserID == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

def update_user(db: Session, user_id: int, user: schemas.UserCreate):
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

# ROOM CRUD
def create_room(db: Session, room: schemas.RoomCreate):
    db_room = models.Room(**room.dict())
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

def get_room(db: Session, room_id: int):
    return db.query(models.Room).filter(models.Room.RoomID == room_id).first()

def get_rooms(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Room).offset(skip).limit(limit).all()

def update_room(db: Session, room_id: int, room: schemas.RoomCreate):
    db_room = get_room(db, room_id)
    if not db_room:
        return None
    for key, value in room.dict().items():
        setattr(db_room, key, value)
    db.commit()
    db.refresh(db_room)
    return db_room

def delete_room(db: Session, room_id: int):
    db_room = get_room(db, room_id)
    if db_room:
        db.delete(db_room)
        db.commit()
    return db_room

# COURSE CRUD
def create_course(db: Session, course: schemas.CourseCreate):
    db_course = models.Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.CourseID == course_id).first()

def get_courses(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Course).offset(skip).limit(limit).all()

def update_course(db: Session, course_id: int, course: schemas.CourseCreate):
    db_course = get_course(db, course_id)
    if not db_course:
        return None
    for key, value in course.dict().items():
        setattr(db_course, key, value)
    db.commit()
    db.refresh(db_course)
    return db_course

def delete_course(db: Session, course_id: int):
    db_course = get_course(db, course_id)
    if db_course:
        db.delete(db_course)
        db.commit()
    return db_course

# SCHEDULE CRUD
def create_schedule(db: Session, schedule: schemas.ScheduleCreate):
    db_schedule = models.ScheduleTable(**schedule.dict())
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)
    return db_schedule

def get_schedule(db: Session, schedule_id: int):
    return db.query(models.ScheduleTable).filter(models.ScheduleTable.ScheduleID == schedule_id).first()

def get_schedules(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ScheduleTable).offset(skip).limit(limit).all()

def update_schedule(db: Session, schedule_id: int, schedule: schemas.ScheduleCreate):
    db_schedule = get_schedule(db, schedule_id)
    if not db_schedule:
        return None
    for key, value in schedule.dict().items():
        setattr(db_schedule, key, value)
    db.commit()
    db.refresh(db_schedule)
    return db_schedule

def delete_schedule(db: Session, schedule_id: int):
    db_schedule = get_schedule(db, schedule_id)
    if db_schedule:
        db.delete(db_schedule)
        db.commit()
    return db_schedule

def get_schedules_by_room(db: Session, room_id: int, skip: int = 0, limit: int = 10):
    return (
        db.query(models.ScheduleTable)
        .filter(models.ScheduleTable.RoomID == room_id)
        .offset(skip)
        .limit(limit)
        .all()
    )
    
from datetime import datetime

def get_schedules_by_room_and_date_range(
    db: Session, room_id: int, start_date: datetime, end_date: datetime, skip: int = 0, limit: int = 10
):
    return (
        db.query(models.ScheduleTable)
        .filter(
            models.ScheduleTable.RoomID == room_id,
            models.ScheduleTable.Schedule >= start_date,
            models.ScheduleTable.Schedule <= end_date
        )
        .offset(skip)
        .limit(limit)
        .all()
    )


