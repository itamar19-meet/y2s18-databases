
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Student(Base):
	"""
	Create a students table. This table has
	4 columns.

	The first column, student_id is
	the primary key for the table. The second
	column is a string, representing the name of
	the student. The third column is an integer,
	representing the year the student was born. The last
	column is a Boolean, representing whether or not the student
	has completed the lab.
	"""
	__tablename__ = 'students'
	student_id = Column(Integer, primary_key=True)
	name = Column(String)
	year = Column(Integer)
	finished_lab = Column(Boolean)

	def __repr__(self):
		return ("Student Name: {}\n"
				"Student Year: {}\n"
				"Has Finished Lab: {}\n"
				"ID: {}").format(
					self.name,
					self.year,
					self.finished_lab,
					self.student_id)

# Example 1: Show table schema
# print(repr(Student.__table__))

# Example 2: Create a student object
# x = Student(name="Mayuri", year=2)
# print(x)

# Example 3: Another way to create Student object
# x = Student()
# x.name = "Mayuri"
# print(x)

