from fastapi import FastAPI
from .utils import json_to_dict_list
import os
from typing import Optional


script_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(script_dir)
path_to_json = os.path.join(parent_dir, "students.json")


app = FastAPI()


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
def get_stydent_by_id_query(id: Optional[int] = None):
    students = json_to_dict_list(path_to_json)
    if id != None:
        for student in students:
            if student["student_id"] == id:
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
def get_all_students_course(course: int, major: Optional[str] = None, enrollment_year: Optional[int] = 2018):
    students = json_to_dict_list(path_to_json)
    filtered_students = []
    for student in students:
        if student["course"] == course:
            filtered_students.append(student)
        if major:
            filtered_students = [student for student in filtered_students if student['major'].lower() == major.lower()]

        if enrollment_year:
            filtered_students = [student for student in filtered_students if student['enrollment_year'] == enrollment_year]
    
    return filtered_students

