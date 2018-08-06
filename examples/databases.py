from model import Base, Student

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

Example 1: Adding a student to DB
def add_student(name, year, finished_lab):
	"""
	Add a student to the database, given
	their name, year, and whether they have
	finished the lab.
	"""
	student_object = Student(
		name=name,
		year=year,
		finished_lab=finished_lab)
	session.add(student_object)
	session.commit()
add_student("Mayuri", 2, True)

Example 2: Querying first student from DB
def simple_query():
	"""
	Finds the first student in the database
	"""
	student = session.query(
		Student).first()
	return student
print(simple_query())

Example 3: Querying all students from DB
def query_all():
	"""
	Print all the students in the database.
	"""
	students = session.query(Student).all()
	return students
add_student("Emily", 2, False)
print(simple_query())
print(query_all())

Example 4: Get first student from DB,
with a specific name.
def query_by_name(name):
	"""
	Find the first student in the database,
	by their name
	"""
	student = session.query(Student).filter_by(
		name=name).first()
	return student
print(query_by_name("Mayuri"))

Example 5: Delete all students with
a certain name from DB
def delete_student(name):
	"""
	Delete all students with a certain name
	from the database.
	"""
	session.query(Student).filter_by(
		name=name).delete()
	session.commit()
delete_student("Mayuri")

Example 6: Update attribute of student
in the table
def update_lab_status(name, finished_lab):
	"""
	Update a student in the database, with 
	whether or not they have finished the lab
	"""
	student_object = session.query(
		Student).filter_by(
		name=name).first()
	student_object.finished_lab = finished_lab
	session.commit()
update_lab_status("Emily", True)
query_all()