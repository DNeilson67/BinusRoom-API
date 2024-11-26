from fastapi import FastAPI, Depends, HTTPException, Request, Response
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, SessionLocal
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from fastapi import Query

# Initialize database
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:8000" ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# USER Endpoints
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_users(db, skip, limit)

@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    updated_user = crud.update_user(db, user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted_user = crud.delete_user(db, user_id)
    if not deleted_user:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted_user

# ROOM Endpoints
@app.post("/rooms/", response_model=schemas.Room)
def create_room(room: schemas.RoomCreate, db: Session = Depends(get_db)):
    return crud.create_room(db, room)

@app.get("/rooms/{room_id}", response_model=schemas.Room)
def read_room(room_id: int, db: Session = Depends(get_db)):
    room = crud.get_room(db, room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return room

@app.get("/rooms/", response_model=list[schemas.Room])
def read_rooms(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_rooms(db, skip, limit)

@app.put("/rooms/{room_id}", response_model=schemas.Room)
def update_room(room_id: int, room: schemas.RoomCreate, db: Session = Depends(get_db)):
    updated_room = crud.update_room(db, room_id, room)
    if not updated_room:
        raise HTTPException(status_code=404, detail="Room not found")
    return updated_room

@app.delete("/rooms/{room_id}", response_model=schemas.Room)
def delete_room(room_id: int, db: Session = Depends(get_db)):
    deleted_room = crud.delete_room(db, room_id)
    if not deleted_room:
        raise HTTPException(status_code=404, detail="Room not found")
    return deleted_room

# COURSE Endpoints
@app.post("/courses/", response_model=schemas.Course)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    return crud.create_course(db, course)

@app.get("/courses/{course_id}", response_model=schemas.Course)
def read_course(course_id: int, db: Session = Depends(get_db)):
    course = crud.get_course(db, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@app.get("/courses/", response_model=list[schemas.Course])
def read_courses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_courses(db, skip, limit)

@app.put("/courses/{course_id}", response_model=schemas.Course)
def update_course(course_id: int, course: schemas.CourseCreate, db: Session = Depends(get_db)):
    updated_course = crud.update_course(db, course_id, course)
    if not updated_course:
        raise HTTPException(status_code=404, detail="Course not found")
    return updated_course

@app.delete("/courses/{course_id}", response_model=schemas.Course)
def delete_course(course_id: int, db: Session = Depends(get_db)):
    deleted_course = crud.delete_course(db, course_id)
    if not deleted_course:
        raise HTTPException(status_code=404, detail="Course not found")
    return deleted_course

# SCHEDULE Endpoints
@app.post("/schedules/", response_model=schemas.Schedule)
def create_schedule(schedule: schemas.ScheduleCreate, db: Session = Depends(get_db)):
    return crud.create_schedule(db, schedule)

@app.get("/schedules/{schedule_id}", response_model=schemas.Schedule)
def read_schedule(schedule_id: int, db: Session = Depends(get_db)):
    schedule = crud.get_schedule(db, schedule_id)
    if not schedule:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return schedule

@app.get("/schedules/", response_model=list[schemas.Schedule])
def read_schedules(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_schedules(db, skip, limit)

@app.put("/schedules/{schedule_id}", response_model=schemas.Schedule)
def update_schedule(schedule_id: int, schedule: schemas.ScheduleCreate, db: Session = Depends(get_db)):
    updated_schedule = crud.update_schedule(db, schedule_id, schedule)
    if not updated_schedule:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return updated_schedule

@app.delete("/schedules/{schedule_id}", response_model=schemas.Schedule)
def delete_schedule(schedule_id: int, db: Session = Depends(get_db)):
    deleted_schedule = crud.delete_schedule(db, schedule_id)
    if not deleted_schedule:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return deleted_schedule

@app.get("/schedules/room/{room_id}", response_model=list[schemas.Schedule])
def read_schedules_by_room(room_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    schedules = crud.get_schedules_by_room(db, room_id, skip, limit)
    if not schedules:
        raise HTTPException(status_code=404, detail="No schedules found for the specified RoomID")
    return schedules


@app.get("/schedules/room/{room_id}/range", response_model=list[schemas.Schedule])
def read_schedules_by_room_and_date_range(
    room_id: int,
    start_date: datetime = Query(..., description="Start date of the range (YYYY-MM-DDTHH:MM:SS)"),
    end_date: datetime = Query(..., description="End date of the range (YYYY-MM-DDTHH:MM:SS)"),
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    schedules = crud.get_schedules_by_room_and_date_range(db, room_id, start_date, end_date, skip, limit)
    if not schedules:
        raise HTTPException(status_code=404, detail="No schedules found for the specified RoomID and date range")
    return schedules
