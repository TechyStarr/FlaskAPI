from sqlalchemy import create_engine,Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


# creates a database
engine = create_engine("sqlite:///task.db")

# creates sessions based on unique IDs
session = scoped_session(sessionmaker(bind=engine))

# creates the db model
Base = declarative_base()

"""
	class Task:
		id int
		content string
		date_added datetime
		is_complete Boolean
"""

# defining the Task model
class Task(Base):
	__tablename__ = 'tasks'
	id = Column(Integer(), primary_key = True)
	content = Column(String(500), nullable = False)
	date_added = Column(DateTime(), default = datetime.utcnow)
	is_complete = Column(Boolean(), default = False)

	def __repr__(self):
		return f"<Task{self.id}>"

# creates database and binds to the engine, use "python db.py". db is the filename
Base.metadata.create_all(bind=engine)


	