from fastapi import FastAPI, Depends
from .utils import json_to_dict_list
import os
from typing import List, Optional
from .student import Student as SStudent

script_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(script_dir)
path_to_json = os.path.join(parent_dir, "students.json")


app = FastAPI()


class RBStudent:
    def __init__(
        self,
        course: int,
        major: Optional[str] = None,
        enrollment_year: Optional[int] = 2018,
    ):
        self.course: int = course
        self.major: Optional[str] = major
        self.enrollment_year: Optional[int] = enrollment_year


@app.get("/")
def home_page():
    return {"massage": "Привет, habr!"}


@app.get("/student/{student_id}")
def get_stydent_by_id(student_id: int):
    students = json_to_dict_list(path_to_json)
    for student in students:
        if student["student_id"] == student_id:
            return student
    return {}


@app.get("/student")
def get_stydent_by_id_query(student_id: Optional[int] = None):
    students = json_to_dict_list(path_to_json)
    if id != None:
        for student in students:
            if student["student_id"] == student_id:
                return student
    return {}


@app.get("/students")
def get_all_students(course: Optional[int] = None):
    students = json_to_dict_list(path_to_json)
    if course != None:
        return_list = []
        for student in students:
            if student["course"] == course:
                return_list.append(student)
        return return_list
    return students


@app.get("/students/{course}")
def get_all_students_course(request_body: RBStudent = Depends()) -> List[SStudent]:
    students = json_to_dict_list(path_to_json)
    filtered_students = []
    for student in students:
        if student["course"] == request_body.course:
            filtered_students.append(student)

    if request_body.major:
        filtered_students = [student for student in filtered_students if
                             student['major'].lower() == request_body.major.lower()]

    if request_body.enrollment_year:
        filtered_students = [student for student in filtered_students if
                             student['enrollment_year'] == request_body.enrollment_year]

    return filtered_students
